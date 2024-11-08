from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('auction/', include('auction.urls')),
]


