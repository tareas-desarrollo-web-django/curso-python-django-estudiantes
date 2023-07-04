Herencia
==========

La herencia es un mecanismo que permite crear clases, pero no desde cero, sino tomando como base la implementación completa de otra clase llamada ***clase base***.
* Esto permite extener o ramificar el funcionamiento de una clase sin alterarla en absoluto.
* La clase que hereda de la clase base se llama ***sub-clase***.
* Una vez heredando de una clase base, tenemos toda la implementación de esta y podemos añadir atributos, métodos, y también remplazarlos por otros nuevos.
* Al usar un método de una clase, primero se busca en esta misma, y si no se encuentra entonces se busca en la clase base.
* Podemos forzar el uso de métodos de la clase base usando la función `super()`.

Python también soporta un mecanismo llamado ***Herencia múltiple***. 
* En este caso una clase puede heredar de varias clases al mismo tiempo.
* Para determinar cual método se usará, Python genera una lista ordenada llamada Orden de Resolución de Métodos (MRO del inglés).
* Al usar un método, Python revisa las clases del MRO en orden y usa la primera clase que contenga dicho método.


Sintaxis:
----------

* Para heredar la implementación de una clase `ClaseBase`, a una nueva clase `SubClase`, se usa lo siguiente al definir la nueva clase: `class SubClase(ClaseBase)`.
* Para el caso de herencia múltiple, se usa: `class SubClase(ClaseBase1, ClaseBase2, etc)`.
    * La herencia de las clases base ocurrirá en el mismo orden en el que están especificadas.
* Se puede crear una red de herencias de varios niveles, siempre que el MRO esté bien definido de modo que no entre en conflicto.
