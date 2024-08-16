from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioCrearUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')







