from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Actividad, Importancia, Estado


class Nueva(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/nueva.html'
    model = Actividad
    fields = ('titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado')
    success_url = reverse_lazy('actividades:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update({
            'importancias': Importancia.objects.all(),
            'estados': Estado.objects.all(),
            'accion': 'Crear'
        })

        return context

    def form_valid(self, form):
        r""" HttpResponseRedirect"""
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    


class Lista(TemplateView):
    template_name = 'actividades/lista.html'


class Generador(TemplateView):
    template_name = 'actividades/generador.html'


class Detalle(TemplateView):
    template_name = 'actividades/detalle.html'


class Editar(TemplateView):
    template_name = 'actividades/editar.html'


class Eliminar(TemplateView):
    template_name = 'actividades/eliminar.html'







