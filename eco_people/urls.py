from django.urls import path, include

urlpatterns = [
    path('', include('web_site.urls')),
]