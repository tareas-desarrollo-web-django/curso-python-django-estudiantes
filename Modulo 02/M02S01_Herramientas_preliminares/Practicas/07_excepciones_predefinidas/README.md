Excepciones predefinidas
=========================

Para estandarizar el manejo de errores, Python tiene un conjunto de Excepciones predefinidas:
* En lugar de crear nuestras propias excepciones, lo mejor es usar las que vienen predefinidas.
* Siempre es bueno revisar la lista para usar las excepciones predefinidas que mejor expliquen el tipo de error que queremos informar
* La lista es muy grande y se puede consultar en https://docs.python.org/es/3/library/exceptions.html.
* Algunas de las excepciones más comunes son:
    * `IndexError`: se arrojar cuando un indice de una secuencia está fuera de rango.
    * `KeyError`: se arroja cuando la llave de un mapeador (diccionario) no existe.
    * `NotImplementedError`: se arroja cuando un método no está implementado.
    * `TypeError`: se arroja cuando una función recibe un parámetro de tipo incorrecto.
    * `ValueError`: se arroja cuando una función recibe un parámetro de tipo correcto, pero el valor no es válido.


Sintaxis:
----------
* Cuando en un bloque de código hemos detectado un error que no corresponde manejar a dicho bloque, lo mejor es arrojar una excepción. Esto se hace con la sitaxis:
    * `raise Excepcion(*args)`
