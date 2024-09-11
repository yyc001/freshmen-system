from datetime import timedelta
import random
import time
from django.http import JsonResponse

from src.models import GlobalSettings, ManualCheck, StudentInfo, User, UserPrivilege
from src.utils import QuickResponse, commonPage, require_privilege, require_privilege_or

def get_student_fields(request):
    return JsonResponse({
        "result":"success", 
        "fields": StudentInfo.form_fields()
    })

@commonPage
def get_student_list(request, user_self, parameters):
    require_privilege_or(user_self, 
        UserPrivilege.Privilege.ADMIN.value, 
        UserPrivilege.Privilege.INTERVIEWER.value
    )
    return JsonResponse({
        'students': [{
            'uid': student.user.uid,
            'name': student.name,
            'status_name': ManualCheck.objects.get_or_create(user=student.user)[0].status_name()
        } for student in StudentInfo.objects.all()]
    })


@commonPage
def get_student_info(request, user_self, parameters):
    uid = parameters["uid"]
    if uid != user_self.uid:
        require_privilege_or(user_self, 
            UserPrivilege.Privilege.ADMIN.value, 
            UserPrivilege.Privilege.INTERVIEWER.value
        )
    target_user = User.objects.get(uid=uid)
    return JsonResponse(StudentInfo.objects.get_or_create(user=target_user)[0].info_dict())


@commonPage
def set_student_info(request, user_self, parameters):
    if GlobalSettings.objects.get(key='entrance').value == 'close':
        return JsonResponse({
            'result': 'fail',
            'message': '报名通道关闭'
        }, status=403)
    
    uid = parameters["uid"]
    if uid != user_self.uid:
        require_privilege(user_self, UserPrivilege.Privilege.ADMIN.value)
    elif 'tel' in parameters:
        otp = request.session.get('otp', None)
        otp_expire_time = request.session.get('otp-expire', None)
        if parameters['otp'] == otp and float(otp_expire_time) > time.time():
            request.session.pop('otp')
            request.session.pop('otp-expire')
        else:
            return JsonResponse({
                'result': 'fail',
                'message': '验证码错误'
            }, status=403)
    target_user = User.objects.get(uid=uid)
    manual_check,_ = ManualCheck.objects.get_or_create(user=target_user)
    if not manual_check.editable_status():
        return JsonResponse({
            'result': 'fail',
            'message': '当前申请状态不可编辑'
        }, status=403)
    field_names = [field.name for field in StudentInfo._meta.fields]
    print({
        k:v for k,v in parameters.items() if k in field_names
    })
    StudentInfo.objects.update_or_create(user=target_user, defaults={
        k:v for k,v in parameters.items() if k in field_names
    })
    return QuickResponse.success()

@commonPage
def send_otp(request, user_self, parameters):
    otp = request.session.get('otp', None)
    otp_expire_time = request.session.get('otp-expire', 0)
    if otp is None or float(otp_expire_time) < time.time():
        request.session['otp'] = '{:04d}'.format(random.randint(0, 9999))
        request.session['otp-expire'] = time.time() + 60
        # TODO send SMS and remove jsonresponse
    return JsonResponse({
        'OTP': request.session['otp']
    })