from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, View, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Para el envío de email
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pathlib import Path
from email.mime.image import MIMEImage

import datetime
import lorem
import random

from urllib.parse import urlencode

from . import models

class Nueva(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/nueva.html'
    model = models.Actividad
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']
    success_url = reverse_lazy('actividades:lista')

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)

        contexto['importancias'] = models.Importancia.objects.all()
        contexto['estados'] = models.Estado.objects.all()

        return contexto

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)

        # if self.object is not None:
        #     self.enviar_email(self.object, request)

        return resp

    def enviar_email(self, actividad, request):
        # URLs que serán enviadas al contexto de la plantilla
        urls = {
            "home": request.build_absolute_uri(reverse("core:home")),
            'detalle': request.build_absolute_uri(reverse('actividades:detalle', args=(actividad.id,)))
        }
        # Contexto que será enviado a la plantilla, la cual será renderizada a un string mediante `render_to_string`
        contexto = {'urls':urls, 'actividad':actividad}

        # Preparamos el contenido del correo
        subject = 'Actividades - Nueva actividad registrada'
        from_email = settings.EMAIL_HOST_USER
        to_mail = [settings.EMAIL_HOST_USER]
        # Renderizamos la plantilla del correo con el contexto
        html_content = render_to_string('actividades/email.html', contexto)
        text_content = "\n".join([l for l in map(str.strip, strip_tags(html_content).split("\n")) if l != ""])

        # Creamos el correo con el contenido en texto plano y adjuntamos el contenido HTML
        msg = mail.EmailMultiAlternatives(subject, text_content, from_email, to_mail)
        msg.attach_alternative(html_content, "text/html")
        
        with open(Path(__file__).parent/"static"/"actividades"/"img"/"logo_sm_white.png", 'rb') as f:
            msg_img = MIMEImage(f.read(), _subtype="png")
        # En la plantilla, para usar la imagen debe de ser mediante src="cid:ID", en nuestro caso 
        # src="cid:logo_sm_white.png", 'cid' viene de ContentID.
        msg_img.add_header('Content-ID', '<logo_sm_white.png>')
        # Adjuntamos la imagen en el correo
        msg.attach(msg_img)

        msg.send()


class EmailAux(TemplateView):
    template_name = 'actividades/email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["actividad"] = models.Actividad.objects.all()[0]

        context["urls"] = {
            'home': self.request.build_absolute_uri(reverse('core:home')),
            'detalle': self.request.build_absolute_uri(reverse('core:home')),
        }

        return context
    

class Lista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/lista.html'
    # model = models.Actividad
    context_object_name = 'actividades'
    paginate_by = 3
    # page_kwarg = 'pagina'

    def get_queryset(self):
        importancia_pk = self.request.GET.get('ipk', None)
        estado_pk = self.request.GET.get('epk', None)

        # Si algún ID no es numérico lo hacemos None
        if importancia_pk and not importancia_pk.isdigit():
            importancia_pk = None
        if estado_pk and not estado_pk.isdigit():
            estado_pk = None

        objectos = models.Actividad.objects.filter(usuario=self.request.user)

        # Si hay algun filtro en los parámetros get 'ipk' (importancia pk) y 'epk' (estado pk), lo aplicamos
        if importancia_pk:
            objectos = objectos.filter(importancia=importancia_pk)
        if estado_pk:
            objectos = objectos.filter(estado=estado_pk)

        return objectos
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        get_params = self.request.GET.dict()
        if self.page_kwarg in get_params:
            del get_params[self.page_kwarg]

        context["get_params"] = urlencode(get_params)

        return context
    

class Generador(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/generador.html'

    def post(self, request):
        # Número de actividades indicadas en el formulario
        cantidad = int(request.POST.get('cantidad', 0))
        # Fecha mínima de inicio de las actividades
        fecha_base = datetime.date(year=2024, month=1, day=1)
        # Lista de etiquetas existentes
        et_importancia = models.Importancia.objects.all()
        et_estado = models.Estado.objects.all()

        for _ in range(cantidad):
            actividad = models.Actividad()
            actividad.titulo = lorem.sentence()[0:32]
            actividad.descripcion = lorem.paragraph()
            # Fecha de inicio aleatorio entre 0 y 100 días después de la fecha base
            actividad.fecha_inicio = fecha_base + datetime.timedelta(days=random.randint(0, 100))
            # Fecha límite aleatorio entre 30 y 90 días después de la fecha de inicio
            actividad.fecha_limite = actividad.fecha_inicio + datetime.timedelta(days=random.randint(30, 90))
            # Asignamos la actividad al usario autenticado
            actividad.usuario = request.user
            # Importancia y estado aleatorio
            actividad.importancia = et_importancia[random.randint(0, len(et_importancia) - 1)]
            actividad.estado = et_estado[random.randint(0, len(et_estado) - 1)]
            
            actividad.save()
        
        return redirect('actividades:lista')


class Detalle(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/detalle.html'
    # model = models.Actividad
    # NOTE: Para indicarle a la vista cual es el nombre del parámetro que contiene el ID en la URL
    # por defecto busca el parámetro 'pk'
    # pk_url_kwarg = 'id'

    def get_queryset(self):
        return models.Actividad.objects.filter(usuario=self.request.user)
    

class Editar(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/nueva.html'
    # model = models.Actividad
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']
    # success_url = reverse_lazy('actividades:lista')

    def get_success_url(self):
        return reverse('actividades:detalle', args=(self.kwargs['pk'],))

    def get_queryset(self):
        return models.Actividad.objects.filter(usuario=self.request.user)

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)

        contexto['importancias'] = models.Importancia.objects.all()
        contexto['estados'] = models.Estado.objects.all()

        return contexto


class Eliminar(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/detalle.html'
    success_url = reverse_lazy('actividades:lista')
    extra_context = {'confirmar_eliminar':True}
    # model = models.Actividad

    def get_queryset(self):
        return models.Actividad.objects.filter(usuario=self.request.user)

