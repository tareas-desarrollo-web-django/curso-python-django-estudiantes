Tarjeta - Encapsulamiento
===========================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Tarjeta`:

* El constructor de la clase debe recibir como parámetro un número de tarjeta (str), para almacenarlo como atributo protegido con doble guión bajo.
    * El atributo debe llamarse `__num_tarjeta`.
    * El número de tarjeta puede llevar cualquier tipo y cantidad de espacios
    en cualquier posición.
    * El número de tarjeta dado debe contener 16 dígitos numéricos.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si el número de tarjeta contiene caracteres no numéricos
        * `ValueError`: si el número de tarjeta no contiene 16 dígitos
* La clase debe contener un método con firma `get_tarjeta(self)`.
    * El método debe retornar el número de tarjeta pero con los espacios ya removidos.
* La clase debe contener un método con firma `set_tarjeta(self, num_tarjeta)`.
    * El método debe cambiar el número de tarjeta almacenado en el atributo `__num_tarjeta`.
    * Antes de hacer el cambio se debe revisar contenga 16 dígitos númericos, además de posibles espacios.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si el número de tarjeta contiene caracteres no numéricos
        * `ValueError`: si el número de tarjeta no contiene 16 dígitos

