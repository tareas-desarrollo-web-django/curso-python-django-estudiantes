Clases, objetos e instancias
================================================

En Python, una ***Clase*** es un segmento encapsulado de códido, que describe las características, funciones e interacciones de un objeto.

Un ***Objeto*** es un elemento de código creado a partir de una clase. Cuando creamos un objeto desde una clase, también se dice que el objeto es una ***Instancia*** de la clase.

Los ***atributos*** son variables que están ligadas a objetos, y son usados para almacenar datos esenciales para el funcionamiento de las instancias. Pueden verse como datos o como características del objeto.

Sintaxis:
----------

* Para definir una clase se usa la sintaxis `class NombreDeClase:`.
    * Ejemplo: `class MiClase:`.
* Dentro de la clase se pueden definir variables, funciones, etc. Lo cual veremos más adelante.
* Para crear una instancia de la clase se invoca en nombre de la clase como si fuera una función.
    * Ejemplo: `mi_objeto = MiClase()`
* Para saber si un objeto es una instacia de una clase podemos usar la función predefinida `isinstance`.
    * Ejemplo: `isinstance(5, int)` que resulta en `True`.
* También podemos revisar si un objeto es una instancia de al menos una de varias clases usando el operador de unión `|`.
    * Ejemplo: `isinstance("3.23", float|str)` o `isinstance(3.23, float|str)`, ambas resultan `True`.
* Una clase en sí es un nuevo tipo de dato, por lo que podemos consultar el tipo de dato de un objeto con la función predefinida `type`.
    * Ejemplo: `type("hola")` resulta en `<class 'str'>`.
* Para saber el nombre de una clase usamos el atributo mágico `__name__` sobre la clase.
    * Ejemplo: `MiClase.__name__`
* Para obtener la clase de la cual es instancia un objeto usamos el atributo mágico `__class__`, pero esta vez sobre el objeto, no sobre la clase.
    * Ejemplo: `mi_objeto.__class__`
