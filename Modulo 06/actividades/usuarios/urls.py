from django.urls import path

from . import views

app_name = 'usuarios'
urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro')
]



