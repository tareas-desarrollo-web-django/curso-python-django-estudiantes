from django.urls import path

from . import views

app_name = 'actividades'
urlpatterns = [
    path('email/', views.Email.as_view(), name='email'),
    path('nueva/', views.Nueva.as_view(), name='nueva'),
    path('lista/', views.Lista.as_view(), name='lista'),
    path('generador/', views.Generador.as_view(), name='generador'),
    path('detalle/<int:pk>/', views.Detalle.as_view(), name='detalle'),
    path('editar/<int:pk>/', views.Editar.as_view(), name='editar'),
    path('eliminar/<int:pk>/', views.Eliminar.as_view(), name='eliminar'),
]












