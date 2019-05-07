from django import forms

from captcha.fields import CaptchaField

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=4)
    password2 = forms.CharField(required=True, min_length=4)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class UserInfoForm(forms.Form):
    username = forms.CharField(required=False)
    phone_num = forms.CharField(required=False)
    nick_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)


class ChangeImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']
