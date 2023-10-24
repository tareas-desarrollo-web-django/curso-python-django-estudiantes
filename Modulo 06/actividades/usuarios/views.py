from django.shortcuts import render
from django.http import HttpResponse

import pdb


# Create your views here.
def registro(request):
    if request.method == "GET":
        return render(request, 'usuarios/registro.html')
    elif request.method == "POST":
        print(request.POST)
        return HttpResponse('Formulario enviado')




