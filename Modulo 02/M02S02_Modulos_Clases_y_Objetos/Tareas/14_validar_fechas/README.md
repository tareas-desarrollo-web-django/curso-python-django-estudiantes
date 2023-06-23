Validar fechas
========================

El paquete `datetime` contiene una función llamada `strptime(fecha:str, formato:str)`.
Dicha función sirve para convertir una fecha dada como texto en un objeto 
`datetime`. La estructura de la fecha se puede indicar en el parámetro `formato`.

El formato para una fecha de tipo `dd/mm/aaaa` es `"%d/%m/%Y"`.

Se pueden encontrar más códigos de formato en:
https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Fecha`:

* El constructor de la clase debe recibir como parámetro una fecha en formato `"dd/mm/aaaa"`, para guardarla como atributo.
    * La fecha puede contener espacios al principio y al final.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si la fecha no tiene el formato indicado.
* Dicha clase debe contener un método con firma `valida(self)`.
    * Dicho método debe devolver `True` si la fecha dada es válida o `False`
    si no lo es. Por ejemplo, `"20/12/2022"` es una fecha válida, pero `"32/14/2022"` no es una fecha válida.
