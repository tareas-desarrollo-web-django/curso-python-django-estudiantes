from django.db import models




class Tarea(models.Model):
    titulo = models.CharField(max_length=256, null=False, verbose_name="título")
    descripcion = models.TextField(verbose_name="descripción")
    fecha_inicio = models.DateField(verbose_name="fecha inicio")
    fecha_limite = models.DateField(verbose_name="fecha límite")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")

