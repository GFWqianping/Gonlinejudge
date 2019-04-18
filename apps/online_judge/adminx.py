import xadmin
from xadmin import views

from .models import User, VerifyCode, Problem, SubmitRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'GOnlineJudge后台管理系统'
    site_footer = 'GOnlineJudge'
    menu_style = 'accordion'
    # model折叠


class UserAdmin(object):
    list_display = ('id', 'name', 'email', 'password', 'gender', 'phone_number', 'add_time')
    search_fields = ('id', 'name', 'email', 'password', 'gender', 'phone_number')
    list_filter = ('id', 'name', 'email', 'password', 'gender', 'phone_number', 'add_time')


class VerifyCodeAdmin(object):
    list_display = ('code', 'phone_number', 'add_time')
    search_fields = ('code', 'phone_number')
    list_filter = ('code', 'phone_number', 'add_time')


class ProblemAdmin(object):
    list_display = ('id', 'title', 'content', 'input_sample', 'output_sample', 'add_time')
    search_fields = ('id', 'title', 'content', 'input_sample', 'output_sample')
    list_filter = ('id', 'title', 'content', 'input_sample', 'output_sample', 'add_time')


class SubmitRecordAdmin(object):
    list_display = ('id', 'problem_id', 'user_id', 'record', 'status', 'add_time')
    search_fields = ('id', 'problem_id', 'user_id', 'record', 'status')
    list_filter = ('id', 'problem_id__id', 'user_id__id', 'record', 'status', 'add_time')


xadmin.site.register(User, UserAdmin)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(Problem, ProblemAdmin)
xadmin.site.register(SubmitRecord, SubmitRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
