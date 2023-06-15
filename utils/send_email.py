from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


def send_email(subject, email, template_name, context, from_email=None, **kwargs):
    """
    发送邮件
    :param subject: 邮件主题
    :param email: 收件人邮箱
    :param template_name: 邮件模板
    :param context: 邮件模板上下文
    :param from_email: 发件人邮箱
    :param kwargs: 其他参数
    :return: None
    """
    if from_email is None:
        from_email = ' '
    message = render_to_string(template_name, context=context)
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[email], **kwargs)


def send_active_email(request, user):

    # 发送邮件
    subject = 'DjangoBlog博客系统注册激活邮件'
    # email = user.email
    email = ''
    template_name = 'user/send_active_email.html'
    # 生成token
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    # 激活链接
    url = reverse('user:active', kwargs={'uidb64': uid, 'token': token})
    # 获取当前站点
    site = get_current_site(request)
    # 激活链接
    active_url = 'http://{site}{url}'.format(site=site, url=url)
    context = {
        'user': user,
        'active_url': active_url
    }
    send_email(subject=subject, email=email, template_name=template_name, context=context)

def send_activation_email(user):
    # 生成激活链接的参数
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    domain = get_current_site(request).domain

    # 构建激活链接
    activation_link = f'http://{domain}/activate/{uid}/{token}/'

    # 构建邮件内容
    subject = 'Activate Your Account'
    message = render_to_string('account/activation_email.html', {'activation_link': activation_link})
    from_email = 'noreply@example.com'
    recipient_list = [user.email]

    # 发送邮件
    send_mail(subject, message, from_email, recipient_list)

