Auto-representación de objetos
===============================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Esfera`:

* El constructor de la clase debe recibir como parámetro el radio de la esfera (float), el peso de la esfera (float) y el color de la esfera (str), en ese orden, para almacenarlos como atributos.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si el radio de la esfera es negativo
        * `ValueError`: si el peso de la esfera es negativo
* La clase debe implementar el método mágico `__repr__(self)` para devolver una representación ejecutable para recrear el objeto.
    * El texto que retorne debe poder copiarse y pegarse en el intérprete de Python y eso debe crear un objeto idéntico. Es decir, debe retornar algo idéntico a: `'Esfera(66, 22, "verde")'`, notemos que el color debe estar entre comillas dobles.
    * De preferencia usa el atributo `__class__` en lugar escribir manualmente el nombre de la clase.
