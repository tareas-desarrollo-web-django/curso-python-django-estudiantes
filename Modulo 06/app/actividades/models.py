from django.db import models
from django.contrib.auth.models import User
from django.utils import timesince

class Importancia(models.Model):
    titulo = models.CharField(max_length=32, null=False, verbose_name='título')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='fecha creación')

    def __str__(self):
        return self.titulo

class Estado(models.Model):
    titulo = models.CharField(max_length=32, null=False, verbose_name='título')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='fecha creación')

    def __str__(self):
        return self.titulo

class Actividad(models.Model):
    titulo = models.CharField(max_length=32, null=False, verbose_name='título')
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    fecha_inicio = models.DateField(verbose_name='fecha de inicio')
    fecha_limite = models.DateField(verbose_name='fecha límite')
    importancia = models.ForeignKey(Importancia, on_delete=models.CASCADE, verbose_name='importancia')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name='estado')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='fecha creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='fecha creación')

    def __str__(self):
        return self.titulo

    @property
    def time_since(self):
        return timesince.timesince(self.fecha_creacion)

