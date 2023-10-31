from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

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

    def dispatch(self, request, *args, **kwargs):
        print(f"Cerrando la sesión de {request.user.username}")
        resp = super().dispatch(request, *args, **kwargs)
        print(f"Cerrando la sesión de {request.user.username}")

        return resp


class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:cerrar_sesion')


