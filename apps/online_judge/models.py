from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=12)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=8, choices=(('male', '男'), ('female', '女')))
    phone_number = models.IntegerField()
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=128)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=16, verbose_name='验证码')
    phone_number = models.IntegerField()

    add_time = models.DateTimeField(default=datetime.now)
    #编译时间，非添加时间

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class Problem(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.TextField(max_length=64)
    content = models.TextField()
    input_sample = models.TextField()
    output_sample = models.TextField()

    add_time = models.DateTimeField(default=datetime.now)
    # 编译时间，非添加时间

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SubmitRecord(models.Model):
    """
    提交记录
    """
    RECORD_STATUS = (
        (0, 'Accepted'),
        (1, 'Wrong Answer'),
        (2, 'Time Limit Exceeded'),
        (3, 'Memory Limit Exceeded')
    )
    id = models.IntegerField(unique=True, primary_key=True)
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)
    record = models.TextField(verbose_name='提交记录')
    status = models.CharField(max_length=8, choices=RECORD_STATUS)

    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '提交记录'
        verbose_name_plural = verbose_name








