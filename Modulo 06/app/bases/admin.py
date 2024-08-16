from django.contrib import admin

from . import models


# Configuración del modelo Tarea para el panel de administrador
class TareaAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion', )
    # Columnas a mostrar en la tabla
    list_display = ('titulo', 'fecha_inicio', 'fecha_limite', 'fecha_creacion')
    # Orden jerárquico de las columnas en la tabla. Usar '-' para invertir el orden.
    ordering = ('-fecha_creacion',)

admin.site.register(models.Tarea, TareaAdmin)

