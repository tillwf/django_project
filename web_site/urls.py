from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landpage),
    url('home', views.home, name='home'),
    url('login', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url('logout', auth_views.logout, {'next_page': 'login'}, name='logout'),
    #url('admin', admin.site.urls),
    url('signup', views.signup, name='signup')
]