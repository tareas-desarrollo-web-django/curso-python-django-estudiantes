from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, FileResponse

# Para el email
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pathlib import Path
from email.mime.image import MIMEImage

# Para la vista del generador
import lorem
import datetime
import random

# Para la vista de detalle
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
import io

from .models import Actividad, Importancia, Estado

import pdb


class Email(TemplateView):
    template_name = 'actividades/email.html'

    def get_context_data(self, *args, **kwargs):
        # pdb.set_trace()
        contexto = super().get_context_data(*args, **kwargs)

        actividad = Actividad.objects.filter(id=1)[0]
        urls = {
            "home": self.request.build_absolute_uri(reverse("core:home")),
            'detalle': self.request.build_absolute_uri(reverse('actividades:detalle', args=(actividad.id,)))
        }

        contexto.update({'urls': urls, 'actividad':actividad})

        return contexto


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


class Lista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/lista.html'
    # model = Actividad
    context_object_name = 'actividades'
    paginate_by = 3
    page_kwarg = 'pagina'

    def get_queryset(self):
        importancia_pk = self.request.GET.get('ipk', None)
        estado_pk = self.request.GET.get('epk', None)

        if importancia_pk and not importancia_pk.isdigit():
            importancia_pk= None
        if estado_pk and not estado_pk.isdigit():
            estado_pk= None
        
        actividades = Actividad.objects.filter(usuario=self.request.user)

        if importancia_pk:
            actividades = actividades.filter(importancia=importancia_pk)
        if estado_pk:
            actividades = actividades.filter(estado=estado_pk)

        return actividades
        
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        get_params = '&'.join([f'{p}={k}' for p,k in self.request.GET.items() if p != self.page_kwarg])
        contexto['get_params'] = get_params
        
        return contexto


class Generador(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/generador.html'

    def post(self, request):
        cantidad = int(request.POST.get('cantidad', 0))

        # La fecha de inicio de cada actividad será un día aleatorio entre 'fecha_base' y 100 días después
        fecha_base = datetime.date(year=2023, month=1, day=1)

        et_importancia = Importancia.objects.all()
        et_estado = Estado.objects.all()

        for _ in range(cantidad):
            actividad = Actividad()
            actividad.titulo = lorem.sentence()
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


class Detalle(DetailView):
    template_name = 'actividades/detalle.html'
    model = Actividad
    # Cambiar el nombre a la variable de contexto
    # context_object_name = 'instancia'
    # Contexto extra
    # extra_context = {}
    # Especificar otro nombre de la variable que contiene el pk en la URL
    # pk_url_kwarg = 'object_id'

    def post(self, request, *args, **kwargs):
        descargar = (request.POST['accion'] == 'descargar')

        actividad = self.get_object()

        buffer = self.generar_pdf(actividad)
        
        return FileResponse(buffer, as_attachment=descargar, filename='actividad.pdf')

    def generar_pdf(self, actividad):
        # Buffer de escritura
        buffer = io.BytesIO()
        # Canvas sobre el que escribiremos el PDF
        pdf = canvas.Canvas(buffer, pagesize=pagesizes.letter)

        # Linea actual de escritura de arriba a abajo
        linea = 3
        # Puntos de alto por cada linea
        linea_puntos = 14
        # Margen izquierdo desde donde se iniciará la escritura en cada linea
        inicio_linea = 30
        
        # Escribimos el contenido de la actividad en el PDF
        pdf.drawString(inicio_linea, 780 - linea * linea_puntos, "Titulo:")
        linea += 1
        pdf.drawString(inicio_linea, 780 - linea * linea_puntos, actividad.titulo)
        linea += 2
        pdf.drawString(inicio_linea, 780 - linea * linea_puntos, "Descripción:")
        linea += 1
        # Para la descripción separaremos todo en lineas de 10 palabras
        palabras = actividad.descripcion.split()
        i = 0
        while i < len(palabras):
            pdf.drawString(inicio_linea, 780 - linea * linea_puntos, ' '.join(palabras[i:min(i + 10, len(palabras))]))
            linea += 1
            i += 10
        linea += 1

        pdf.drawString(inicio_linea, 780 - linea * linea_puntos, f"Fecha de inicio: {actividad.fecha_inicio.strftime('%d/%m/%Y')}")
        linea += 2
        pdf.drawString(inicio_linea, 780 - linea * linea_puntos, f"Fecha límite: {actividad.fecha_limite.strftime('%d/%m/%Y')}")
        linea += 2

        pdf.drawString(inicio_linea, 780 - linea * linea_puntos, f"Importancia: {actividad.importancia}")
        linea += 2
        pdf.drawString(inicio_linea, 780 - linea * linea_puntos, f"Estado: {actividad.estado}")
        linea += 2

        # Volcamos el PDF en el buffer
        pdf.showPage()
        pdf.save()

        # Posicionamos el cursero del buffer al inicio para que el FileResponse pueda usarlo
        buffer.seek(0)

        return buffer



class Editar(TemplateView):
    template_name = 'actividades/editar.html'


class Eliminar(TemplateView):
    template_name = 'actividades/eliminar.html'







