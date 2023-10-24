from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings as django_settings


# Create your views here.
def settings(request):
    return HttpResponse(django_settings.ENTORNO)