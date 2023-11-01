r"""
Ajustes the producción
"""
from .comunes import *
try:
    from .host import *
except ImportError:
    ...

ENTORNO = "Estoy en modo Producción"

DEBUG = False

ALLOWED_HOSTS = ['*']



