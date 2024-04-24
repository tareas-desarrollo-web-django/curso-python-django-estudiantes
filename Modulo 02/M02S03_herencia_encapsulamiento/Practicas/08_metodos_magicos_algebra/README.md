Métodos mágicos (dunder) para emular álgebra
===================================================

Aquí continuamos con los métodos mágicos (o dunder), pero ahora veremos algunos que se suelen usar para que un objeto soporte operaciones algebráicas personalizadas.

Sintaxis:
----------

* `__neg__`: dar soporte para cambiar el signo al objeto en cuestión, con el operador unario `-`.
* `__add__`: agregar soporte para sumar un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `+`.
* `__sub__`: agregar soporte para restar un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `-`.
* `__mul__`: agregar soporte para multiplicar un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `*`.
* `__truediv__`: agregar soporte para dividir un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `/`.
* `__floordiv__`: agregar soporte para dividir a piso un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `//`.
* `__lt__`: agregar soporte para comparar si el objeto en cuestión es menor que un objeto del mismo o de diferente tipo, con el operador `<`.
* `__le__`: agregar soporte para comparar si el objeto en cuestión es menor o igual que un objeto del mismo o de diferente tipo, con el operador `<=`.
* `__gt__`: agregar soporte para comparar si el objeto en cuestión es mayor que un objeto del mismo o de diferente tipo, con el operador `>`.
* `__ge__`: agregar soporte para comparar si el objeto en cuestión es mayor o igual que un objeto del mismo o de diferente tipo, con el operador `>=`.
* `__eq__`: agregar soporte para comparar si el objeto en cuestión es igual que un objeto del mismo o de diferente tipo, con el operador `==`.
* `__ne__`: agregar soporte para comparar si el objeto en cuestión es diferente que un objeto del mismo o de diferente tipo, con el operador `!=`.
