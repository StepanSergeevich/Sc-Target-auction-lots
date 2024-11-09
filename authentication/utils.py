from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
import secrets


#Код для верификации почты
def generate_confirmation_code():
    return secrets.token_hex(16)

#Форма отправки и отправка кода на почту пользователя authentication
def send_confirmation_email(user_email, confirmation_code):  
    subject = 'Подтверждение регистрации ScAuction'
    html_content = render_to_string('authentication/email_sending.html', {'code': confirmation_code})
    plain_message = strip_tags(html_content)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(
        subject,
        plain_message,  # Текстовая версия письма
        email_from,
        recipient_list,
        fail_silently=False,
        html_message=html_content  # HTML-контент
    )

