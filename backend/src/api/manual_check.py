from django.http import JsonResponse

from src.models import Attachments, GlobalSettings, ManualCheck, StudentInfo, User, UserPrivilege
from src.utils import ErrorPacketExamples, PrivilegeException, QuickResponse, commonPage, require_privilege, require_privilege_or


@commonPage
def get_materials_status(request, user_self, parameters):
    uid = parameters["uid"]
    target_user = User.objects.get(uid=uid)
    if uid != user_self.uid:
        require_privilege_or(user_self, 
            UserPrivilege.Privilege.ADMIN.value, 
        )
    student_info, _ = StudentInfo.objects.get_or_create(user=target_user)
    REQUIRED_DOMAIN = {
        'name': '姓名',
        'gender': '性别',
        'campus': '校区',
        'photo': '证件照',
        'service_hall_app_no': '服务大厅申请编号'
    }
    info_str = "、".join([v for k,v in REQUIRED_DOMAIN.items() if getattr(student_info, k) is None])
    attachment_names = [attachment.filename for attachment in Attachments.objects.filter(user=target_user).all()]
    REQUIRED_FILE = {
        student_info.name + '-自荐信.pdf': '自荐信',
    }
    attach_str = "、".join([v for k,v in REQUIRED_FILE.items() if k not in attachment_names])
    return JsonResponse({
        "tel": "已验证" if student_info.tel else "未验证",
        "info": "缺少必填项：" + info_str if info_str else "基本信息齐全",
        "attachments": "缺少必需附件：" + attach_str if attach_str else "附件齐全",
        'complete': student_info.tel and not info_str and not attach_str
    })
    


@commonPage
def get_manual_check_result(request, user_self, parameters):
    uid = parameters["uid"]
    target_user = User.objects.get(uid=uid)
    if uid != user_self.uid:
        require_privilege_or(user_self, 
            UserPrivilege.Privilege.ADMIN.value, 
            UserPrivilege.Privilege.INTERVIEWER.value
        )
        return JsonResponse(ManualCheck.objects.get_or_create(user=target_user)[0].info_dict(private=True))
    return JsonResponse(ManualCheck.objects.get_or_create(user=target_user)[0].info_dict())
    

@commonPage
def set_manual_check_result(request, user_self, parameters):
    require_privilege(user_self, UserPrivilege.Privilege.ADMIN.value)
    target_user = User.objects.get(uid=parameters['uid'])
    field_names = [field.name for field in ManualCheck._meta.fields]
    ManualCheck.objects.update_or_create(user=target_user, defaults={
        k:v for k,v in parameters.items() if k in field_names
    })
    return QuickResponse.success()


@commonPage
def self_change_manual_check(request, user_self, parameters):
    if user_self.uid != parameters['uid']:
        raise PrivilegeException(ErrorPacketExamples.NoPrivilege)
    if GlobalSettings.objects.get(key='entrance').value == 'close':
        return JsonResponse({
            'result': 'fail',
            'message': '报名通道关闭'
        }, status=403)
    
    manual_check, _ = ManualCheck.objects.get_or_create(user=user_self)
    if manual_check.editable_status() and parameters['to'] == ManualCheck.Status.WAITING.value:
        manual_check.submission_times += 1
        manual_check.status = ManualCheck.Status.WAITING.value
    elif not manual_check.editable_status() and parameters['to'] == ManualCheck.Status.REVOKED.value:
        manual_check.status = ManualCheck.Status.REVOKED.value
    manual_check.save()
    return QuickResponse.success()
