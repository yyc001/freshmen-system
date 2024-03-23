import json
from json import JSONDecodeError

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden

from app.settings import DEBUG
from src.models import User, UserPrivilege


class ErrorPacket:
    def __init__(self, errcode, err_message):
        self._errcode = errcode
        self._err_message = err_message

    def get_errcode(self):
        return self._errcode

    def get_err_message(self):
        return self._err_message

    def __str__(self):
        return self._err_message


class MyExceptionFactory(Exception):
    def __init__(self, error_packet: ErrorPacket):
        self._err_message = error_packet.get_err_message()
        self._errcode = error_packet.get_errcode()

    def __str__(self):
        return self._err_message

    def errcode(self):
        return self._errcode


class PrivilegeException(MyExceptionFactory):
    pass


class ErrorPacketExamples:
    NoPrivilege = ErrorPacket(500, "无权限")
    ConditionNotSatisfied = ErrorPacket(508, "条件不满足")
    AlreadyExists = ErrorPacket(509, "已添加，请勿重复添加")


class QuickResponse:
    @classmethod
    def not_support(cls):
        return JsonResponse({
            'result': 'fail',
            'message': '不支持的操作'
        }, status=405)

    @classmethod
    def success(cls):
        return JsonResponse({
            'result': 'success'
        })

    @classmethod
    def not_logged_in(cls):
        return JsonResponse({
            'result': 'fail',
            'message': '未登录'
        }, status=401)

    @classmethod
    def no_privilege(cls):
        return HttpResponseForbidden()

    @classmethod
    def hint(cls, message):
        return JsonResponse({
            "result": "success",
            "hint": message
        })

    @classmethod
    def handle_exception(cls, exception: Exception):
        if isinstance(exception, KeyError):
            return JsonResponse({
                "result": "fail",
                "message": "缺少参数： " + "; ".join(exception.args)
            }, status=400)
        elif isinstance(exception, ObjectDoesNotExist):
            return JsonResponse({
                "result": "fail",
                "message": "对象不存在： " + "; ".join(exception.args)
            }, status=400)
        elif isinstance(exception, IntegrityError):
            return JsonResponse({
                "result": "fail",
                "message": "数据已存在： " + "; ".join(exception.args)
            }, status=400)
        elif isinstance(exception, PrivilegeException):
            return JsonResponse({
                "result": "fail",
                "message": str(exception)
            }, status=403)
        else:
            if DEBUG:
                raise exception
            else:
                return JsonResponse({
                    "result": "fail",
                    "message": "错误： " + "; ".join(exception.args)
                }, status=403)


def autoHandleException(func):
    def decorated(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Exception as e:
            return QuickResponse.handle_exception(e)

    return decorated


def debugOnly(func):
    def decorated(*args, **kwargs):
        if DEBUG:
            return func(*args, **kwargs)
        else:
            return HttpResponseNotFound

    return decorated


def get_dict_from_request(request):
    # all_dict = request.GET
    if request.method == "POST":
        try:
            text = json.loads(request.body)
        except JSONDecodeError:
            text = request.POST.dict()
        return {**request.GET.dict(), **text}
    else:
        return request.GET.dict()


def requireLoggedIn(func):
    def decorated(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return QuickResponse.not_logged_in()
        return func(request, *args, **kwargs)

    return decorated


# mix of requireLoggedIn + autoHandleException
def commonPage(func):
    def decorated(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                with transaction.atomic():
                    user_self, _ = User.objects.get_or_create(uid=request.user.username)
                    parameters = get_dict_from_request(request)
                    ret = func(request, user_self, parameters, *args, **kwargs)
                return ret
            else:
                return QuickResponse.not_logged_in()
        except Exception as e:
            return QuickResponse.handle_exception(e)

    return decorated


def require_privilege(user, *privilege_list):
    for privilege in privilege_list:
        if UserPrivilege.objects.filter(user=user, privilege=privilege).count() == 0:
            raise PrivilegeException(ErrorPacketExamples.NoPrivilege)
        
        
def require_privilege_or(user, *privilege_list):
    for privilege in privilege_list:
        if UserPrivilege.objects.filter(user=user, privilege=privilege).count() > 0:
            return
    raise PrivilegeException(ErrorPacketExamples.NoPrivilege)