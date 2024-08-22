from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, View, ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Para el envío de email
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pathlib import Path
from email.mime.image import MIMEImage

from . import models

class Nueva(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/nueva.html'
    model = models.Actividad
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']
    success_url = reverse_lazy('core:home')

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
    paginate_by = 2
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
    


class Generador(View):
    ...


class Detalle(View):
    ...


class Editar(View):
    ...


class Eliminar(View):
    ...

