from django.urls import path

from .views import registro

app_name = 'usuarios'
urlpatterns = [
    path('registro/', registro, name='registro')
]



