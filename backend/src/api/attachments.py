from django.http import FileResponse, JsonResponse

from src.models import Attachments, GlobalSettings, ManualCheck, User, UserPrivilege
from src.utils import QuickResponse, commonPage, require_privilege, require_privilege_or, requireLoggedIn


@commonPage
def get_file_list(request, user_self, parameters):
    uid = parameters["uid"]
    if uid != user_self.uid:
        require_privilege_or(user_self, 
            UserPrivilege.Privilege.ADMIN.value, 
            UserPrivilege.Privilege.INTERVIEWER.value
        )
    attachments = Attachments.objects.filter(
        user=User.objects.get(uid=uid)
    )   
    return JsonResponse({
        "attachments": [{
            'uid': attachment.file_id,
            'name': attachment.filename,
            'url': f'/api/student/attachments/download?id={attachment.file_id}'
        } for attachment in attachments]
    })


# @require_http_methods(['POST'])
@requireLoggedIn
def upload(request):
    if GlobalSettings.objects.get(key='entrance').value == 'close':
        return JsonResponse({
            'result': 'fail',
            'message': '报名通道关闭'
        }, status=403)
    user_self = User.objects.get(uid=request.user.username)
    manual_check,_ = ManualCheck.objects.get_or_create(user=user_self)
    if not manual_check.editable_status():
        return JsonResponse({
            'result': 'fail',
            'message': '当前申请状态不可编辑'
        }, status=403)
    
    file_req = request.FILES.get('file')
    if file_req:
        attachment = Attachments.objects.create(
            user=user_self,
            filename=file_req.name,
            file=file_req
        )
        return JsonResponse({
            "success": True,
            "url": f'/api/student/attachments/download?id={attachment.file_id}',
            'uid': attachment.file_id
        })
    return JsonResponse({
        'success': False
    })


@commonPage
def download(request, user_self, parameters):
    id = parameters['id']
    attachment = Attachments.objects.get(file_id=id)
    if attachment.user.uid != user_self.uid:
        require_privilege_or(user_self, 
            UserPrivilege.Privilege.ADMIN.value, 
            UserPrivilege.Privilege.INTERVIEWER.value
        )
    return FileResponse(
        attachment.file.open(),
        filename=attachment.filename, 
        as_attachment=True
    )


@commonPage
def remove(request, user_self, parameters):
    if GlobalSettings.objects.get(key='entrance').value == 'close':
        return JsonResponse({
            'result': 'fail',
            'message': '报名通道关闭'
        }, status=403)
    id = parameters['id']
    attachment = Attachments.objects.get(file_id=id)
    if attachment.user.uid != user_self.uid:
        require_privilege(user_self, 
            UserPrivilege.Privilege.ADMIN.value, 
        )
    target_user = User.objects.get(uid=attachment.user.uid)
    manual_check,_ = ManualCheck.objects.get_or_create(user=target_user)
    if not manual_check.editable_status():
        return JsonResponse({
            'result': 'fail',
            'message': '当前申请状态不可编辑'
        }, status=403)
    
    attachment.delete()
    return QuickResponse.success()
    
