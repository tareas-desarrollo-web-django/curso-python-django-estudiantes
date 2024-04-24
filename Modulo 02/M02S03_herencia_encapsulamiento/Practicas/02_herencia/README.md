Herencia
==========

La herencia es un mecanismo que permite crear clases, pero no desde cero, sino tomando como base la implementación completa de otra clase llamada ***clase base***.
* Esto permite extender o ramificar el funcionamiento de una clase sin alterar la primera en absoluto.
* La clase que hereda de la clase base se llama ***sub-clase***.
* Una vez heredando de una clase base, tenemos toda la implementación de esta y podemos añadir atributos, métodos, y también remplazarlos por otros nuevos.
* Al usar un método de una clase, primero se busca en esta misma, y si no se encuentra entonces se busca en la clase base.
* Podemos forzar el uso de métodos de la clase base usando la función `super()`.

Sintaxis:
----------

* Para heredar la implementación de una clase `ClaseBase`, a una nueva clase `SubClase`, se usa lo siguiente al definir la nueva clase: `class SubClase(ClaseBase)`.
