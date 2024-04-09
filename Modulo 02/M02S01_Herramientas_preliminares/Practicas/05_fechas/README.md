Fechas con `datetime` y `pytz`
==================================

Python contiene integrada una librería llamada `datetime` para manipular fechas de manera muy sencilla:
* Ya viene integrada en Python, no hay que instalarla.
* Sirve para crear fechas a partir de texto.
* Convierte fechas `datetime` a texto en el formato que queramos.
* Sumar días, minutos, segundos, etc. a fechas.
* Calcular diferencias de tiempo entre fechas.

Por otro lado, la librería `pytz` es utilizada para manejar zonas horarias:
* No viene instalada en Python, hay que instalarla: `pip install pytz`.
* Contiene la base de datos de las zonas horarias del mundo.

Sintaxis:
---------

Los objetos y funciones básicos son:
* `datetime.datetime`: objeto para manipular fechas
* `datetime.timedelta`: objeto para almacenar diferencias de tiempo
* `datetime.datetime.now()`: obtiene la fecha y hora de este momento
* `datetime.datetime.strptime()`: crea una fecha desde texto
* `datetime.datetime.strftime()`: convierte una fecha a texto
* `pytz.timezone.localize()`: asigna una zona horaria a una fecha.
* `pytz.timezone.astimezone()`: convierte una fecha a otra zona horaria.
