from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pathlib import Path
from email.mime.image import MIMEImage

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

    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)

        if self.object is not None:
            self.enviar_email(request, self.object)
        
        return resp
    
    def enviar_email(self, request, actividad):
        # Preparamos las urls que insertaremos en la plantilla del correo
        urls = {
            "home": request.build_absolute_uri(reverse("core:home")),
            'detalle': request.build_absolute_uri(reverse('actividades:detalle', args=(actividad.id,)))
        }

        # Renderizamos la plantilla del correo con las urls y los datos de la actividad
        subject = 'Actividades - Nueva actividad registrada'
        from_email = settings.EMAIL_HOST_USER
        to_mail = [settings.EMAIL_HOST_USER]
        html_content = render_to_string('actividades/email.html', {'urls':urls, 'actividad':actividad})
        text_content = "\n".join([l for l in map(str.strip, strip_tags(html_content).split("\n")) if l != ""])

        # Creamos el correo
        msg = mail.EmailMultiAlternatives(subject, text_content, from_email, to_mail)
        msg.attach_alternative(html_content, "text/html")
        # msg.mixed_subtype = 'related'

        # La plantilla usa una imagen, para que pueda reconocerla debemos adjuntarla al correo, en modo invisible
        with open(Path(__file__).parent/"static"/"actividades"/"img"/"logo_sm_white.png", 'rb') as f:
            msg_img = MIMEImage(f.read(), _subtype="png")
        msg_img.add_header('Content-ID', '<logo_sm_white.png>')
        msg.attach(msg_img)

        msg.send()


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







