from django.urls import path, include

from .views import ChangePwdView, UserInfoView, ChangeImageView, ShowRecords


urlpatterns = [
    path('', UserInfoView.as_view(), name='user_info'),
    path('change/pwd/', ChangePwdView.as_view(), name='change_pwd'),
    path('change/image/', ChangeImageView.as_view(), name='change_img'),
    path('records/', ShowRecords.as_view(), name='show_records')
]
