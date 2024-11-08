from django.core.mail import send_mail
from django.conf import settings
import requests
import secrets


#Код для верификации почты
def generate_confirmation_code():
    return secrets.token_hex(16)

#Форма отправки и отправка кода на почту пользователя
def send_confirmation_email(user_email, confirmation_code):
    subject = 'Подтверждение регистрации ScAuction'
    message = f'Ваш код подтверждения: {confirmation_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)

# Получение токена
def get_token():
    token_url = "https://exbo.net/oauth/token"
    API_KEY = 'cTn0PHFRazfucUZJNxHTEOoOVxYYrgeXXKtycoZn'

    data = {
        'client_id': "277",
        'client_secret': f'{API_KEY}',
        'grant_type': 'client_credentials',
        'scope': "",
    }

    response = requests.post(token_url, data=data)

    return response.json()

