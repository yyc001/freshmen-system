from django.urls import path

from src.api import basic, globals, stu_info, manual_check, attachments

urlpatterns = [
    path('showrequest', basic.show_request),
    path('install', basic.install),
    path('login_debug', basic.login_debug),
    path('login_root', basic.login_root),
    path('logout', basic.logout),
    path('install', basic.install),
    path('whoami', basic.who_am_i),
    # path('upload', basic.upload),

    path('global/set', globals.global_settings),
    path('global/get', globals.get_open_time),

    path('student/list', stu_info.get_student_list),
    path('student/info/fields', stu_info.get_student_fields),
    path('student/info/get', stu_info.get_student_info),
    path('student/info/set', stu_info.set_student_info),
    path('student/otp', stu_info.send_otp),

    path('student/check/get', manual_check.get_manual_check_result),
    path('student/check/set', manual_check.set_manual_check_result),
    path('student/check/change', manual_check.self_change_manual_check),
    path('student/check/info', manual_check.get_materials_status),

    path('student/attachments/get', attachments.get_file_list),
    path('student/attachments/upload', attachments.upload),
    path('student/attachments/download', attachments.download),
    path('student/attachments/remove', attachments.remove),
]
