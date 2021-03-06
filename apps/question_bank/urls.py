from django.urls import path, include

from question_bank.views import QuestionHomeView, AnswerView


urlpatterns = [
    path('', QuestionHomeView.as_view(), name='question_home'),
    path('<int:pk>/', AnswerView.as_view(), name='answer')
    # path('change/pwd/', ChangePwdView.as_view(), name='change_pwd'),
    # path('change/image/', ChangeImageView.as_view(), name='change_img')
]
