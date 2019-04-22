from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from online_judge.models import UserProfile
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) |
                                           Q(email=username) |
                                           Q(phone_number=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def g_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'emsg':'用户名或密码错误'})
    elif request.method == 'get':
        return render(request, 'login.html')


