import json

from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

from .models import User, EmailVerifyCode
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm, UserInfoForm, ChangeImageForm
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {'username': username})
                else:
                    return render(request, 'login.html', {'emsg': '用户未激活'})

            else:
                return render(request, 'login.html', {'emsg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            username = request.POST.get('username', '')
            if User.objects.filter(email=email):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '此邮箱已被注册'})
            if User.objects.filter(username=username):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '此用户名已被注册'})
            password = request.POST.get('password', '')
            user = User()
            user.username = username
            user.email = email
            user.is_active = False
            user.password = make_password(password)
            user.save()

            send_register_email(email, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyCode.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = User.objects.get(email=email)
                if user:
                    user.is_active = True
                    user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'active_fail.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm(request.POST)
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, send_type='forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetPwdView(View):
    def get(self, request, reset_code):
        modify_pwd_form = ModifyPwdForm()
        all_records = EmailVerifyCode.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'modifypwd.html', {'modify_pwd_form': modify_pwd_form})
        else:
            return render(request, 'active_fail.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_pwd_form = ModifyPwdForm(request.POST)
        email = request.POST.get('email', '')
        if modify_pwd_form.is_valid():
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            if password1 != password2:
                return render(request, 'modifypwd.html',
                              {'modify_pwd_form': modify_pwd_form, 'email': email, 'msg': '密码不一致'})
            user = User.objects.get(email=email)
            user.password = make_password(password1)
            user.save()
            return render(request, 'login.html', )
        else:
            return render(request, 'modifypwd.html',
                          {'modify_pwd_form': modify_pwd_form, 'email': email})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')


class UserInfoView(LogoutView, View):
    def get(self, request):
        return render(request, 'usercenter-info.html')

    def post(self, request):
        user_info_form = UserInfoForm(request.POST)
        if user_info_form.is_valid():
            # img = request.POST.get('image', '')
            nick_name = request.POST.get('nick_name', '')
            gender = request.POST.get('gender')
            phone_num = request.POST.get('phone_num')
            # email = request.POST.get('email')
            username = request.POST.get('username')

            user = User.objects.get(username=username)
            user.nick_name = nick_name
            # user.image = img
            user.gender = gender
            user.phone_number = phone_num
            user.save()
            return render(request, 'usercenter-info.html')
        else:
            return render(request, 'usercenter-info.html', {'user_info_form': user_info_form})


class ChangePwdView(View):
    def post(self, request):
        change_pwd_form = ModifyPwdForm(request.POST)
        if change_pwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type='application/json')
            user = request.user
            user.password = make_password(pwd2)
            user.save()

            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(change_pwd_form.errors), content_type='application/json')


class ChangeImageView(LogoutView, View):

    def post(self, request):
        image_form = ChangeImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')

