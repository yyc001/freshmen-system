from django.http import JsonResponse

from src.models import GlobalSettings, UserPrivilege
from src.utils import QuickResponse, commonPage, require_privilege, require_privilege_or



@commonPage
def global_settings(request, user_self, parameters):
    require_privilege(user_self, UserPrivilege.Privilege.ADMIN.value)
    for k,v in parameters.items():
        GlobalSettings.objects.update_or_create(key=k, defaults={"value": v})

    return QuickResponse.success()



@commonPage
def get_open_time(request, user_self, parameters):
    start_time = GlobalSettings.objects.get(key="start-time").value
    end_time = GlobalSettings.objects.get(key="end-time").value
    entrance = GlobalSettings.objects.get(key="entrance").value

    return JsonResponse({
        "start_time": start_time,
        "end_time": end_time,
        "entrance": entrance
    })