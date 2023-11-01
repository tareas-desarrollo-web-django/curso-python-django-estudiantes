from django.contrib.auth.models import User
from django.db import models
from django.utils import timesince


class Importancia(models.Model):
    titulo = models.CharField(max_length=32, null=False, blank=False, verbose_name='título')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='fecha actualización')

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Etiqueta de importancia'
        verbose_name_plural = 'Etiquetas de importancia'
        ordering = ['-fecha_creacion']


class Estado(models.Model):
    titulo = models.CharField(max_length=32, null=False, blank=False, verbose_name='título')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='fecha actualización')

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Etiqueta de estado'
        verbose_name_plural = 'Etiquetas de estado'
        ordering = ['-fecha_creacion']


class Actividad(models.Model):
    titulo = models.CharField(max_length=256, null=False, verbose_name="título")
    descripcion = models.TextField(verbose_name="descripción")
    fecha_inicio = models.DateField(verbose_name="fecha inicio")
    fecha_limite = models.DateField(verbose_name="fecha límite")
    importancia = models.ForeignKey(Importancia, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='fecha actualización')

    def __str__(self):
        return self.titulo
    
    @property
    def registrada_desde(self):
        return timesince.timesince(self.fecha_creacion)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['-fecha_creacion']



