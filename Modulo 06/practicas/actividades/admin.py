from django.contrib import admin

from . import models


class ImportanciaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

class EstadoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

class ActividadAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    # Columnas a mostrar en la tabla
    list_display = ('titulo', 'importancia', 'estado', 'fecha_inicio', 'fecha_limite', 'fecha_creacion', 'usuario')
    # Orden jerárquico de las columnas en la tabla. Usar '-' para invertir el orden.
    ordering = ('-fecha_actualizacion',)
    # Campos de búsqueda para la tabla
    # Para campos que son otras clases, eg. relaciones ForeignKey, se usa '__' para consultar el campo anidado
    # Ejemplo: 'campo_clase__id'
    search_fields = ('titulo',)
    # Campo para crear una jerarquía de fechas de filtro rápido (por mes y luego por día)
    date_hierarchy = 'fecha_inicio'
    # Campos de filtros
    list_filter = ('importancia', 'estado')


admin.site.register(models.Importancia, ImportanciaAdmin)
admin.site.register(models.Estado, EstadoAdmin)
admin.site.register(models.Actividad, ActividadAdmin)


