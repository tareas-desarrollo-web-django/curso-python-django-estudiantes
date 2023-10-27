from django.contrib import admin

from . import models

class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)
    list_display = ('titulo', 'descripcion', 'fecha_inicio', 'fecha_limite')
    ordering = ('-fecha_creacion',)



admin.site.register(models.Tarea, TareaAdmin)


