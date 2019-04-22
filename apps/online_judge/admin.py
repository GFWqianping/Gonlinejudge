from django.contrib import admin

# Register your models here.

from online_judge.models import UserProfile


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserAdmin)
