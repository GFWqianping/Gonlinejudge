from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=12)


class User(AbstractUser):
    # id = models.IntegerField(unique=True, primary_key=True)
    nick_name = models.CharField(max_length=32, default='', verbose_name='昵称')
    email = models.CharField(max_length=64, null=True, blank=True, default='邮箱地址')
    gender = models.CharField(max_length=8, choices=(('male', '男'), ('female', '女')),
                              default='male', verbose_name='性别')
    phone_number = models.CharField(default='', verbose_name='电话', max_length=16)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=128)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name != '':
            return self.nick_name
        else:
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


class EmailVerifyCode(models.Model):
    """
    电子邮件验证码
    """
    code = models.CharField(max_length=16, verbose_name='验证码')
    email = models.EmailField(max_length=64, verbose_name='邮箱')
    send_type = models.CharField(verbose_name='验证码类型',
                                 choices=(('register', '注册'), ('forget', '忘记密码')),
                                 default='register', max_length=16)
    send_time = models.DateTimeField(verbose_name='发送时间', default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Problem(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.TextField(max_length=64)
    content = models.TextField(verbose_name='题目描述')
    input_sample = models.TextField(verbose_name='样例输入')
    output_sample = models.TextField(verbose_name='样例输出')

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
        (-1, 'WRONG_ANSWER'),
        (0, 'ACCEPTED'),
        (1, 'CPU_TIME_LIMIT_EXCEEDED'),
        (2, 'REAL_TIME_LIMIT_EXCEEDED'),
        (3, 'MEMORY_LIMIT_EXCEEDED'),
        (4, 'RUNTIME_ERROR'),
        (5, 'SYSTEM_ERROR'),
        (6, 'WAITING'),
    )
    id = models.CharField(primary_key=True, unique=True, max_length=32)
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    record = models.TextField(verbose_name='提交记录')
    status = models.CharField(max_length=8, choices=RECORD_STATUS, default=6)
    language = models.CharField(max_length=16, default='python', verbose_name='语言',
                                choices=(('Python3', 'Python3'), ('C++', 'C++'),
                                         ('Java', 'Java'), ('C', 'C'), ('Python2', 'Python2')))
    time_cost = models.IntegerField(default=0)
    memory_cost = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '提交记录'
        verbose_name_plural = verbose_name








