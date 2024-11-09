from .views import change_password, fetch_lots_data
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'), #Главная страница
    path('logout/', views.logout_view, name='logout'), #Выход с аккаунтта 
    path('profile_user/', views.profile_user, name='profile_user'), #Настройки провиля пользователя
    path('change_password/', change_password.as_view(), name='change_password'), #Смена пароля пользователя
    path('profile_user/choice_lots/', views.choice_lots, name='choice_lots'), #Настройки вывода лотов
    path('main/fetch_lots_data/', fetch_lots_data, name='fetch_lots_data'), # Обновление лотов на главной странице
]