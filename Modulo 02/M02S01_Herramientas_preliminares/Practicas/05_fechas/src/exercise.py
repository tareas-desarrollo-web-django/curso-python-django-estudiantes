from datetime import datetime, timedelta
from pytz import timezone

##############################################################################
# Definiciones



# Obtenemos la fecha y hora de este momento
ahora = datetime.now()
# Eliminamos las horas, minutos, etc y solo consevamos día, mes y año
hoy = ahora.replace(hour=0, minute=0, second=0, microsecond=0)
# Otra forma de obtener la fecha de hoy con cero horas, minutos y segundos
hoy = datetime.combine(ahora, datetime.min.time())

# Obtenemos la fecha de mañana
manana = hoy + timedelta(days=1)

# Creamos un datetime con la fecha de navidad
navidad = datetime.strptime("25/12/2024", "%d/%m/%Y")
# Último día de agosto del 2024
fin_agosto = datetime.strptime("01/09/2024", "%d/%m/%Y") - timedelta(days=1)
# Fecha inicializada con valores numéricos
dia_independencia = datetime(year=2023, month=9, day=16)

##############################################################################
# Operaciones

# Número de días para que llegue navidad
dias_para_navidad = (navidad - hoy).days
print(f"Días para navidad: {dias_para_navidad}")

# Último día de agosto del 2024 en formato "dd/mm/aaaa"
fin_agosto_texto = fin_agosto.strftime("%d/%m/%Y")
print(f"Último día de agosto del 2024: {fin_agosto_texto}")

# Revisar si una fecha está entre hoy y navidad
print(f"Dia de Independencia entre hoy y navidad?: {hoy <= dia_independencia  <= navidad}")

##############################################################################
# Zonas horarias
# Podemos ver la lista de Códigos IANA en: https://timeapi.io/documentation/iana-timezones
# Podemos consultar la lista soportada por `pytz` con: `pytz.all_timezones`

# Para crear un objeto de zona horaria tenemos que usar su código IANA
tz_cdmx = timezone('America/Mexico_City')
tz_madrid = timezone('Europe/Madrid')

# Asignamos la zona horaria a la hora de ahorita
ahora_en_mexico = tz_cdmx.localize(ahora)
print(ahora_en_mexico.strftime('%Y-%m-%d %H:%M:%S'))

# Convertir la hora de México a Madrid
ahora_en_madrid = ahora_en_mexico.astimezone(tz_madrid)
print(ahora_en_madrid.strftime('%Y-%m-%d %H:%M:%S'))

##############################################################################
# Podemos obtener el código de la zona horaria local

from tzlocal import get_localzone

# Obtenemos el código IANA de la zona local
codigo_local = get_localzone().key
tz_local = timezone(codigo_local)

# Obtenemos la fecha y hora y le asignamos la zona horaria local
local_time = tz_local.localize(datetime.now())
# O de forma más directa, el parámetro 'tz' no es soportado por `datetime` ni `datetime.strptime`
local_time = datetime.now(tz=tz_local)

##############################################################################
# Ejemplos de uso

def primer_dia_del_mes(mes, anio, indice_dia):
    r"""
    Primer día semanal del mes/año dado. Por ejemplo, obtener la fecha del
    primer Lunes del mes de Noviembre del 2024. El argumento `indice_dia` 
    es el número de día de la semana en cuestión y representa 
    1=Lunes, ..., 7=Domingo.
    """
    # Fecha del primer día del mes en cuestión
    inicio_mes = datetime(year=anio, month=mes, day=1)
    # Obtenemos el índice del día de la semana del primer día del mes
    # 1=Lunes, ..., 7=Domingo
    indice_inicio_mes = inicio_mes.isoweekday()
    # Número de dias para llegar del inicio del mes al días especificado
    diferencia_dias = indice_dia - indice_inicio_mes
    if diferencia_dias >= 0:
        return inicio_mes + timedelta(diferencia_dias)
    else:
        return inicio_mes + timedelta(diferencia_dias + 7)

