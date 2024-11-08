from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('authentication', views.authentication, name='authentication'), #Регистрация и Авторизация
    path('confirmation', views.verifity_email, name='confirmation'), #Подтверждение почты 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'), #Восстановление пароля 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'), #отправка письма
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'), #Заход пользователя на страницу изменения пароля
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), #пароль изменён
]