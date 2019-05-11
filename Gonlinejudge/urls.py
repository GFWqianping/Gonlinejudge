"""Gonlinejudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import xadmin
# import captcha

from apps.online_judge.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView,\
    ResetPwdView, ModifyPwdView, LogoutView, UserInfoView
from apps.question_bank.views import SubmitRecordView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('active/<str:active_code>/', ActiveUserView.as_view(), name='active'),
    path('reset/<str:reset_code>/', ResetPwdView.as_view(), name='reset_pwd'),
    path('modify/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('user/', include('apps.online_judge.urls')),
    path('question/', include('apps.question_bank.urls')),
    path('record/', SubmitRecordView.as_view(), name='record'),
]
