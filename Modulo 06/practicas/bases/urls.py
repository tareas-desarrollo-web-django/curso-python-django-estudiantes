from django.urls import path

from . import views

app_name = 'bases'
urlpatterns = [
    path('vista_funcion/', views.vista_funcion, name='vista_funcion'),
    path('vista_clase/', views.VistaClase.as_view(), name='vista_clase'),
    path('vista_plantilla/', views.VistaPlantilla.as_view(), name='vista_plantilla'),
    path('mi_plantilla/', views.MiPlantilla.as_view(), name='mi_plantilla'),
    path('django_plantilla/', views.DjangoPlantilla.as_view(), name='django_plantilla'),
    path('crear_tarea/', views.CrearTarea.as_view(), name='crear_tarea'),
]













