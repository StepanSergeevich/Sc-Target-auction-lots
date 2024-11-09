from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('auction/', include('auction.urls')),
    path('admin/', admin.site.urls),
]


