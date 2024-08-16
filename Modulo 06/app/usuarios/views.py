from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
from .forms import FormularioCrearUsuario


class Registro(CreateView):
    template_name = 'usuarios/registro.html'
    # Tiene los campos 'username', 'password1', 'password2'
    form_class = FormularioCrearUsuario
    success_url = reverse_lazy('usuarios:iniciar_sesion')


class IniciarSesion(LoginView):
    template_name = 'usuarios/iniciar_sesion.html'
    next_page = reverse_lazy('core:home')


class CerrarSesion(LogoutView):
    next_page = reverse_lazy('usuarios:iniciar_sesion')


class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:cerrar_sesion')

