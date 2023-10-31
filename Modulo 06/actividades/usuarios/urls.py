from django.urls import path

from . import views

app_name = 'usuarios'
urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro'),
    path('iniciar_sesion/', views.IniciarSesion.as_view(), name='iniciar_sesion'),
    path('cerrar_sesion/', views.CerrarSesion.as_view(), name='cerrar_sesion'),
    path('cambiar_password/', views.CambiarPassword.as_view(), name='cambiar_password'),
]



