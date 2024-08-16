from django.urls import path


from . import views

app_name = 'bases'
urlpatterns = [
    path('vista_funcion/', views.vista_funcion, name='vista_funcion'),
    path('vista_clase/', views.VistaClase.as_view(), name='vista_clase'),
    path('plantilla_index/', views.PlantillaIndex.as_view(), name='plantilla_index'),
    path('plantilla_home/', views.PlatillaHome.as_view(), name='plantilla_home'),
    path('template_index/', views.TemplateIndex.as_view(), name='template_index'),
    path('crear_tarea/', views.CrearTarea.as_view(), name='crear_tarea'),
]





