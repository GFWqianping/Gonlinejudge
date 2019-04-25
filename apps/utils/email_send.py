import random
from django.core.mail import send_mail

from apps.online_judge.models import EmailVerifyCode
from Gonlinejudge.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyCode()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = 'Gonline_judge激活链接'
        email_body = '请点击下面链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(random_length=8):
    code = ''
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    length = len(chars) - 1
    for i in range(random_length):
        code += chars[random.randint(0, length)]
    return code



