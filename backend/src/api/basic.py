import uuid
from django.contrib import auth
from django.contrib.auth.models import User as AuthUser
from django.http import JsonResponse
from django.shortcuts import redirect

from configurations import ROOT_UID
from src.models import GlobalSettings, User, UserPrivilege
from src.utils import debugOnly, get_dict_from_request, autoHandleException, QuickResponse, commonPage


@debugOnly
def show_request(request):
    return JsonResponse({
        'request': get_dict_from_request(request),
        'session': {**request.session},
        "host": request.get_host(),
    })


@debugOnly
@autoHandleException
def login_debug(request):
    parameters = get_dict_from_request(request)
    uid = int(parameters['uid'])
    name = parameters.get('name', '测试用户')

    user, created = AuthUser.objects.get_or_create(username=parameters['uid'])
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)

    User.objects.update_or_create(uid=uid, defaults={"name": name})
    return QuickResponse.success()


@autoHandleException
def login_root(request):
    User.objects.get(uid=ROOT_UID, token=request.GET['token'])

    user, created = AuthUser.objects.get_or_create(username=ROOT_UID)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    return QuickResponse.success()


@commonPage
def logout(request, user_self, parameters):
    auth.logout(request)
    return redirect('/cas/logout')


@debugOnly
def install(request):
    # c64573bf6f804b808605378797fc06b2
    root_token = uuid.uuid4().hex
    user_root = User.objects.create(
        uid=ROOT_UID,
        name='ROOT 教师',
        token=root_token
    )
    UserPrivilege.objects.create(user=user_root, privilege=UserPrivilege.Privilege.ROOT.value)
    UserPrivilege.objects.create(user=user_root, privilege=UserPrivilege.Privilege.ADMIN.value)
    UserPrivilege.objects.create(user=user_root, privilege=UserPrivilege.Privilege.INTERVIEWER.value)
    GlobalSettings.objects.create(key='start-time', value='')
    GlobalSettings.objects.create(key='end-time', value='')
    GlobalSettings.objects.create(key='registration', value='close')
    return JsonResponse({
        "root_token": root_token
    })


def set_csrf_token_into_cookie(request):
    # 获取的同时自动塞入cookie
    # 不要在这里调用get_token()，这么返回的token无效，而set-cookie的有效
    return JsonResponse({})


@commonPage
def who_am_i(request, user_self, parameters):
    return JsonResponse({
        "name": user_self.name,
        "uid": user_self.uid
    })
