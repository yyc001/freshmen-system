import uuid
from django.db import models

from src.constants import GK_LANGUAGES, PROVINCES, YN, AWARDS, MAJORS, COLLEGES, CAMPUSES, GENDERS, EXEMPTIONS


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
    college = models.IntegerField(blank=True, null=True)
    highschool = models.CharField(max_length=255, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    qq = models.IntegerField(blank=True, null=True)
    emergency_tel = models.IntegerField(blank=True, null=True)

    major = models.IntegerField(blank=True, null=True)
    award = models.IntegerField(blank=True, null=True)
    ycjh = models.IntegerField(blank=True, null=True)
    exemption = models.IntegerField(blank=True, null=True)
    exemption_reason = models.CharField(max_length=255, blank=True, null=True)

    gk_province = models.IntegerField(blank=True, null=True)
    gk_overall_a = models.CharField(max_length=255, blank=True, null=True)
    gk_overall_f = models.CharField(max_length=255, blank=True, null=True)
    gk_rank = models.CharField(max_length=255, blank=True, null=True)
    gk_yw_a = models.CharField(max_length=255, blank=True, null=True)
    gk_yw_f = models.CharField(max_length=255, blank=True, null=True)
    gk_sx_a = models.CharField(max_length=255, blank=True, null=True)
    gk_sx_f = models.CharField(max_length=255, blank=True, null=True)
    gk_wy_a = models.CharField(max_length=255, blank=True, null=True)
    gk_wy_f = models.CharField(max_length=255, blank=True, null=True)
    gk_wyyz = models.IntegerField(blank=True, null=True)
    gk_wl_a = models.CharField(max_length=255, blank=True, null=True)
    gk_wl_f = models.CharField(max_length=255, blank=True, null=True)
    gk_hx_a = models.CharField(max_length=255, blank=True, null=True)
    gk_hx_f = models.CharField(max_length=255, blank=True, null=True)
    gk_sw_a = models.CharField(max_length=255, blank=True, null=True)
    gk_sw_f = models.CharField(max_length=255, blank=True, null=True)
    gk_lkzh_a = models.CharField(max_length=255, blank=True, null=True)
    gk_lkzh_f = models.CharField(max_length=255, blank=True, null=True)

    service_hall_app_no = models.CharField(max_length=255, blank=True, null=True)

    def info_dict(self):
        fields = self.__class__._meta.get_fields()
        return { 
            field.name: getattr(self, field.name) 
            for field in fields 
            if field.concrete and field.name != "user"
        }
    
    @classmethod
    def form_fields(cls):
        return [
            {   "name": "p1",
                "label": "第一部分 · 个人信息",
                "type": "title"
            },
            {   "name": "name",
                "label": "姓名",
                "type": "text",
                "help": "若学籍姓名与证件姓名不一致，请及时联系管理员。",
            },
            {   "name": "gender",
                "label": "性别",
                "type": "radio",
                "options": GENDERS
            },
            {   "name": "campus",
                "label": "校区",
                "type": "select",
                "options": CAMPUSES
            },
            {   "name": "college",
                "label": "学院",
                "type": "select",
                "help": "威海校区请从后往前寻找自己的学院",
                "options": COLLEGES
            },
            {   "name": "highschool",
                "label": "来源中学",
                "type": "text",
            },
            {   "name": "photo",
                "label": "标准证件照",
                "type": "profile",
            },
            {   "name": "qq",
                "label": "QQ",
                "type": "text",
                # "pattern": r"[1-9]\d{4,9}",
                "help": "选填，推荐填写。",
                "optional": "true"
            },
            {   "name": "emergency_tel",
                "label": "紧急联系人电话",
                "type": "text",
                "pattern": r"[1-9]\d{10}",
            },
            {   "name": "p2",
                "label": "第二部分 · 报考信息",
                "type": "title"
            },
            {   "name": "major",
                "label": "报考取向",
                "type": "select",
                "options": MAJORS
            },
            {   "name": "award",
                "label": "竞赛获奖",
                "type": "select",
                "help": "还没想好怎么实现<a>示例链接</a>",
                "options": AWARDS
            },
            {   "name": "ycjh",
                "label": "英才计划",
                "type": "select",
                "help": "参加中国科协、教育部“中学生英才计划”，顺利完成对应学科的学业。",
                "options": YN
            },
            {   "name": "exemption",
                "label": "免试资格",
                "type": "select",
                "options": EXEMPTIONS
            },
            {   "name": "exemption_reason",
                "label": "免试理由",
                "type": "text",
                "optional": "true"
            },
            {   "name": "p3",
                "label": "第三部分 · 高考成绩",
                "type": "title"
            },
            {   "name": "gk_province",
                "label": "高考省份",
                "type": "select",
                "options": PROVINCES
            },
            {   "name": "gk_overall",
                "label": "高考总成绩和满分",
                "type": "dtext",
                "split": "/",
                "childnames": [ "gk_overall_a", "gk_overall_f" ]
            },
            {   "name": "gk_rank",
                "label": "高考排名",
                "type": "text",
                "pattern": r"\d{1,6}"
            },
            {   "name": "gk_yw",
                "label": "语文成绩和满分",
                "type": "dtext",
                "split": "/",
                "childnames": [ "gk_yw_a", "gk_yw_f" ]
            },
            {   "name": "gk_sx",
                "label": "数学成绩和满分",
                "type": "dtext",
                "split": "/",
                "childnames": [ "gk_sx_a", "gk_sx_f" ]
            },
            {   "name": "gk_wy",
                "label": "外语成绩和满分",
                "type": "dtext",
                "split": "/",
                "childnames": [ "gk_wy_a", "gk_wy_f" ]
            },
            {   "name": "gk_wyyz",
                "label": "外语语种",
                "type": "select",
                "options": GK_LANGUAGES
            },
            {   "name": "gk_wl",
                "label": "物理成绩和满分",
                "type": "dtext",
                "split": "/",
                "optional": "true",
                "help": "若未选考此科目，或高考无此科目，请留空。",
                "childnames": [ "gk_wl_a", "gk_wl_f" ]
            },
            {   "name": "gk_hx",
                "label": "化学成绩和满分",
                "type": "dtext",
                "split": "/",
                "optional": "true",
                "help": "若未选考此科目，或高考无此科目，请留空。",
                "childnames": [ "gk_hx_a", "gk_hx_f" ]
            },
            {   "name": "gk_sw",
                "label": "生物成绩和满分",
                "type": "dtext",
                "split": "/",
                "optional": "true",
                "help": "若未选考此科目，或高考无此科目，请留空。",
                "childnames": [ "gk_sw_a", "gk_sw_f" ]
            },
            {   "name": "gk_lkzh",
                "label": "理科综合成绩和满分",
                "type": "dtext",
                "split": "/",
                "optional": "true",
                "help": "若未选考此科目，或高考无此科目，请留空。",
                "childnames": [ "gk_lkzh_a", "gk_lkzh_f" ]
            },
        ]
    

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
