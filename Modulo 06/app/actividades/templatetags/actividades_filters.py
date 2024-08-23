from django import template
from datetime import datetime, date

register = template.Library()

@register.filter
def isoformat(valor):
    """ 
    Si `valor` es un datetime lo convierte a texto isoformat, si no entonces
    lo devuelve así mismo.
    """
    if isinstance(valor, datetime|date):
        valor = valor.isoformat()
    
    return valor


