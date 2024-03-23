import uuid
from django.db import models


class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, null=True, blank=True)
    # banned = models.BooleanField(default=False)


class UserPrivilege(models.Model):
    class Privilege(models.IntegerChoices):
        ROOT = 0, 'ROOT'
        STUDENT = 1, '学生'
        ADMIN = 2, '管理员'
        INTERVIEWER = 3, '面试官'

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    privilege = models.IntegerField(choices=Privilege.choices)


class GlobalSettings(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255)


class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    tel = models.CharField(max_length=255, blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    campus = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)

    service_hall_app_no = models.CharField(max_length=255, blank=True, null=True)

    def info_dict(self):
        return {
            "tel": self.tel,
            "name": self.name,
            "gender": self.gender,
            "campus": self.campus,
            "photo": self.photo,
            "service_hall_app_no": self.service_hall_app_no,
        }
    

def custom_upload_to(_, f):
    return 'storage/{}-{}'.format(uuid.uuid4().hex, f)

class Attachments(models.Model):

    file_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to=custom_upload_to)


class ManualCheck(models.Model):

    ALLOW_REQUEST_TIMES = 3

    class Status(models.IntegerChoices):
        UNSUBMITTED = 0, '未提交'
        WAITING = 1, '审核中'
        PASSED = 2, '已通过'
        FAIL = 3, '未通过'
        REVOKED = 4, '已撤销'

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    submission_times = models.IntegerField(default=0)
    status = models.IntegerField(default=0, choices=Status.choices)
    comment = models.CharField(max_length=255)
    private_comment = models.CharField(max_length=255)

    def editable_status(self):
        return self.status in [
            self.__class__.Status.UNSUBMITTED.value,
            self.__class__.Status.FAIL.value,
            self.__class__.Status.REVOKED.value,
        ]
    
    def revokable_status(self):
        return self.status in [
            self.__class__.Status.WAITING.value,
            self.__class__.Status.PASSED.value,
        ]
    
    def info_dict(self, private=False):
        return {
            'remain': self.__class__.ALLOW_REQUEST_TIMES - self.submission_times,
            'comment': self.comment,
            'private_comment': self.private_comment if private else '*',
            'allow_submit': self.editable_status() and \
                self.submission_times < self.__class__.ALLOW_REQUEST_TIMES,
            'allow_revoke': self.revokable_status(),
            'status': self.status,
            'status_name': self.status_name(),
        }
    
    def status_name(self):
        return self.__class__.Status(self.status).label
