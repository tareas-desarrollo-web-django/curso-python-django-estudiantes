from django.urls import path

from . import views


app_name = 'actividades'
urlpatterns = [
    path('nueva/', views.Nueva.as_view(), name='nueva'),
    path('email_aux/', views.EmailAux.as_view(), name='email_aux'),
]





