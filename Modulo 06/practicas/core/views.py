from django.shortcuts import render
from django.views.generic import RedirectView
from django.http import HttpResponse


class Home(RedirectView):
    pattern_name = 'actividades:lista'

