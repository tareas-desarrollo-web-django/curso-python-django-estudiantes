from django.contrib import admin

from . import models

class ImportanciaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)

class EstadoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)

class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('titulo', 'importancia', 'estado', 'fecha_inicio', 'fecha_limite', 'fecha_creacion', 'usuario')
    ordering = ('-fecha_actualizacion',)
    search_fields = ('titulo',)
    date_hierarchy = 'fecha_inicio'
    list_filter = ('importancia', 'estado')

admin.site.register(models.Importancia, ImportanciaAdmin)
admin.site.register(models.Estado, EstadoAdmin)
admin.site.register(models.Actividad, ActividadAdmin)
