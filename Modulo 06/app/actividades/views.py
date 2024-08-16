from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import models

class Nueva(CreateView):
    template_name = 'actividades/nueva.html'
    model = models.Actividad
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']
    success_url = reverse_lazy('core:home')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto['importancias'] = models.Importancia.objects.all()
        contexto['estados'] = models.Estado.objects.all()

        return contexto







