from django.urls import path, include

from .views import ChangePwdView, UserInfoView, ChangeImageView


urlpatterns = [
    path('', UserInfoView.as_view(), name='user_info'),
    path('change/pwd/', ChangePwdView.as_view(), name='change_pwd'),
    path('change/image/', ChangeImageView.as_view(), name='change_img')
]
