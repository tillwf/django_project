from django.contrib import admin
from django.urls import path, include
from web_site import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landpage),
    path('web_site/', include('web_site.urls')),
]
