from .views import change_password
from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.user_lots, name='main'), #Главная страница
    path('logout/', views.logout_view, name='logout'), #Выход с аккаунтта 
    path('profile_user/', views.profile_user, name='profile_user'), #Настройки провиля пользователя
    path('change_password/', change_password.as_view(), name='change_password'), #Смена пароля пользователя
    path('profile_user/choice_lots/', views.choice_lots, name='choice_lots'), #Настройки вывода лотов
]