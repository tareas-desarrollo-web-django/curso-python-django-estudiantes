from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=256, null=False, verbose_name='título')
    descripcion = models.TextField(verbose_name="descripción", null=True, blank=True)
    fecha_inicio = models.DateField(verbose_name="fecha inicio")
    fecha_limite = models.DateField(verbose_name="fecha límite")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")

    def __str__(self):
        return self.titulo
    

