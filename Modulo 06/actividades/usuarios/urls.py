from django.urls import path

from .views import settings

app_name = 'usuarios'
urlpatterns = [
    path('settings/', settings, name='settings')
]



