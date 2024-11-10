from pathlib import Path
import os 

#API STALCRAFT
API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyNzciLCJqdGkiOiI5YjA5MDA2MmZmMzQwMTYxZWY5YTU4N2E3MGY3MTYzMDZhOGNhMGUyNTYyZDJmNjU3ZDljMjJiMzE4MmI1NDc5OTc0ODYxMTY0YmY3MWFjYiIsImlhdCI6MTczMTAwMTQ3OS40ODYyODEsIm5iZiI6MTczMTAwMTQ3OS40ODYyODQsImV4cCI6MTc2MjUzNzQ3OS4yOTA1ODksInN1YiI6IiIsInNjb3BlcyI6W119.UyQ8SYZuYZF2Y47bEYT6t_F2krKDRgcXGzQ-Kr1wssd5JaL7q0qVNs91a7HgOXIizlngfzmIl0AQ-GgFgwqqujIGYTnpWS8bTpvkie0mxnsnl0s42h_EF5TcuYPxpS-4eYPB8nmNlQZDaPGBnq8UCEvVzHRrx4PAm3t2z4_0hGPpvBqjkK_7aGnJ0V1QCAzhQlG0X3W-xaVvTrgwRu1f8yH3t0I8lMXlcu784Lo9aehuNXX0lOlbx1r8TF6TXpH2SHaBI0cvRlsdQ9CdUCEDZPSexIjYwnot9FqXdIewlAMw6j_hs7JUJpBEhJUxDpENgSe3E-W75eOiJXHInAoAVEh3xzU2b2k7PWljurANJosXzw55vor2ZROJaUFxMgRPQIYsRDeGVSAwaLoZFGfLSKHG2wwkYMzU1euqG3IHjDzLKFWi_dU5ARDRvN9klIquuyCsP1amgT5c9Bp-gneUlcU-tqpnWBeFzvG39JseVIPp4h0HZ3AsFIM5Xd0xGrr0P_yN9brAcAj4NfcZrrXnQ7Sbgdql9M0boJrgJiDb30zj4rFr8VdSiV-0PHLFzuzLeGd_tWBmw-u_hpJ-CyfRM_WiMAdoBOIkkC3RuxBKi_G6CVEEGFOEZaLEwXr_WRVizUWFKUHFrNwnSfzjoC0THoxL9ouafBZiadaez3QkiM8'

DEBUG = True
LOGIN_URL = '/auth/authentication'
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'StalcraftAuction.urls'
BASE_DIR = Path(__file__).resolve().parent.parent
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  
EMAIL_HOST_USER = 'StalcraftAuction@yandex.ru'
EMAIL_HOST_PASSWORD = 'sldsmwmmpdptfpjf'
DEFAULT_FROM_EMAIL = 'StalcraftAuction@yandex.ru'
WSGI_APPLICATION = 'StalcraftAuction.wsgi.application'
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SECRET_KEY = 'django-insecure-sjc-9di+c8a9x@-@_svh+q*6=ts7nih!gq_$hxsrc*^8jfpj0%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  
        'USER': 'postgres',        
        'PASSWORD': '123', 
        'HOST': 'localhost',   # db - Для docker'a        
        'PORT': '5432',                 
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'auction',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auction.middleware.LoginRequiredMiddleware',
    'auction.middleware.ErrorLoggingMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'authentication/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]



