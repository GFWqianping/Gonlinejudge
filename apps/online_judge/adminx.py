import xadmin
from xadmin import views

from .models import EmailVerifyCode,  SubmitRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'GonlineJudge后台管理系统'
    site_footer = 'GonlineJudge'
    menu_style = 'accordion'
    # model折叠


class UserAdmin(object):
    list_display = ('id', 'name', 'email', 'password', 'gender', 'phone_number', 'add_time')
    search_fields = ('id', 'name', 'email', 'password', 'gender', 'phone_number')
    list_filter = ('id', 'name', 'email', 'password', 'gender', 'phone_number', 'add_time')


class EmailVerifyCodeAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time')
    search_fields = ('code', 'email', 'send_type')
    list_filter = ('code', 'email', 'send_type', 'send_time')


class ProblemAdmin(object):
    list_display = ('id', 'title', 'content', 'input_sample', 'output_sample', 'add_time')
    search_fields = ('id', 'title', 'content', 'input_sample', 'output_sample')
    list_filter = ('id', 'title', 'content', 'input_sample', 'output_sample', 'add_time')


class SubmitRecordAdmin(object):
    list_display = ('id', 'problem_id', 'user_id', 'record', 'status', 'add_time', 'language')
    search_fields = ('id', 'problem_id', 'user_id', 'record', 'status', 'language')
    list_filter = ('id', 'problem_id__id', 'user_id__id', 'record', 'status', 'add_time', 'language')


xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
xadmin.site.register(SubmitRecord, SubmitRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
