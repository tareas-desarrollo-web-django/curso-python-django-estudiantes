from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, CreateView

from .models import Tarea


def vista_funcion(request):
    tarjetas = range(1, 11)
    if request.method == 'GET':
        return render(request, 'bases/index.html', {'tarjetas':tarjetas})
    elif request.method == 'POST':
        return render(request, 'bases/index.html', {'tarjetas':tarjetas, 'mensaje':request.POST})


class VistaClase(View):
    def get(self, request):
        return render(request, 'bases/index.html', {'tarjetas':range(1, 11)})

    def post(self, request):
        return render(request, 'bases/index.html', {'tarjetas':range(1, 11), 'mensaje':request.POST})


class VistaPlantilla(View):
    plantilla = None
    nombre_formulario = 'formulario'
    contexto_extra = {}

    def get(self, request):
        return render(request, self.plantilla, self.contexto_extra)
    
    def post(self, request):
        contexto = {self.nombre_formulario:request.POST}
        contexto.update(self.contexto_extra)
        return render(request, self.plantilla, contexto)


class PlantillaIndex(VistaPlantilla):
    plantilla = 'bases/index.html'
    nombre_formulario = 'mensaje'
    contexto_extra = {'tarjetas':range(1, 11)}


class PlatillaHome(VistaPlantilla):
    plantilla = 'bases/home.html'
    contexto_extra = {'textos': ['Soy texto 1', 'Soy texto 2', 'Soy texto 3', 'Soy texto 4']}


class TemplateIndex(TemplateView):
    template_name = 'bases/index.html'
    extra_context = {'tarjetas':range(1, 11)}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user.username if self.request.user.is_authenticated else 'anónimo'
        return context

    def post(self, request):
        contexto = self.get_context_data()
        contexto['mensaje'] = request.POST
        return render(request, self.template_name, contexto)


class CrearTarea(CreateView):
    template_name = 'bases/crear_tarea.html'
    model = Tarea
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite']
    success_url = reverse_lazy('bases:crear_tarea')


