Herencia
==========

Además de la herencia regular, Python también soporta un mecanismo llamado ***Herencia múltiple***:
* En este caso una clase puede heredar de varias clases al mismo tiempo.
* Para determinar cual método se usará, Python genera una lista ordenada llamada Orden de Resolución de Métodos (MRO del inglés).
* Al usar un método o atributo, Python revisa las clases del MRO en orden y usa la primera clase que contenga dicho método o atributo.
* Para ejecutar desde nuestra clase un método correspondiente a una de las clases bases en particular se puede seguir usando `super`, pero con la siguiente sintaxis: `super(ClaseBase, self)`, donde indicamos la clase base a usar para buscar el método.


Sintaxis:
----------

* Para el caso de herencia múltiple, se usa la siguiente sintaxis: `class SubClase(ClaseBase1, ClaseBase2, etc)`.
* La herencia será aplicada en el mismo orden en el que están especificadas las clases base.
* Se puede crear una red de herencias de varios niveles, siempre que el MRO esté bien definido de modo que no entre en conflicto.
* Para revisar el orden de resolución MRO de una clase, podemos usar el método `clase.mro()`, que es definido automáticamente por Python.


