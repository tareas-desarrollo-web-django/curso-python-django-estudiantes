Atributos dinámicos de objetos
================================

Python tiene una libertad muy grande al implementar código. Un ejemplo de esto es que a los objetos se les puede agregar y borrar atributos dinámicamente, similar a los diccionarios.

Esto aplica también a las clases, ya que, por mas extraño que parezca, las clases también son objetos, es por eso que pueden tener atributos.


Sintaxis:
----------

* Para agregar un atributo a un objeto, solo basta con asignarle un valor, cuando Python nota que no existe, entonces lo crea solo para el objeto en cuestión.
    * Ejemplo: `MiObjeto.nuevo_atributo = 10`
* Para eliminar un atributo de un objeto, usamos la palabra `del`.
    * Ejemplo: `del MiObjeto.nuevo_atributo`.