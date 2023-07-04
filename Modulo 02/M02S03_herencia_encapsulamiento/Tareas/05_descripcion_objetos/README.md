Auto-descripción de objetos
============================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Esfera`:

* El constructor de la clase debe recibir como parámetro el radio de la esfera (float), el peso de la esfera (float) y el color de la esfera (str), en ese orden, para almacenarlos como atributos.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si el radio de la esfera es negativo
        * `ValueError`: si el peso de la esfera es negativo
* La clase debe implementar el método mágico `__str__(self)` para devolver una representación amigable del objeto.
    * La representación debe ser similar a la forma: `"{radio:5, peso:1, color:verde}"`. Notemos que el color no contiene las comillas.
