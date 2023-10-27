from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

import pdb



class Registro(CreateView):
    template_name = 'usuarios/registro.html'
    # Este formulario espera los campos 'username', 'password1' y 'password2'
    form_class = UserCreationForm
    success_url = reverse_lazy('usuarios:registro')



