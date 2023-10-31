from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

import pdb



class Registro(CreateView):
    template_name = 'usuarios/registro.html'
    # Este formulario espera los campos 'username', 'password1' y 'password2'
    form_class = UserCreationForm
    success_url = reverse_lazy('usuarios:iniciar_sesion')


class IniciarSesion(LoginView):
    template_name = 'usuarios/iniciar_sesion.html'
    next_page = reverse_lazy('core:home')


class CerrarSesion(LogoutView):
    next_page = reverse_lazy('usuarios:iniciar_sesion')


class CambiarPassword(View):
    def get(self, request):
        return HttpResponse('Vista de Cambiar Password')


