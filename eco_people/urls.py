from django.contrib import admin
from django.urls import path, include
from web_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('web_site/', include('web_site.urls'))
]