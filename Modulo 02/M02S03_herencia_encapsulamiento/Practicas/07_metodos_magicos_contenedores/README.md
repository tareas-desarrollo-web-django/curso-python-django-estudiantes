Métodos mágicos (dunder) para simular contenedores
===================================================

Aquí continuamos con los métodos mágicos (o dunder), pero ahora veremos algunos que se suelen usar para que un objeto se comporte como si fuera un contenedor.

Sintaxis:
----------

* `__len__`: debe devolver el número de elementos que simula tener el contendor, se invoca automáticamente al usar la función `len()` sobre un objeto.
* `__getitem__`: debe devolver una referencia al elemento asociado a la llave (o índice). Se invoca automáticamente al consultar con el operador `[]`.
    * Ejemplo: `mi_objeto[5]`, o `mi_objeto["a"]`, etc.
* `__setitem__`: debe asignar un nuevo valor al elemento asociado a la llave (o índice). Se invoca automáticamente al asignar valores con el operador `[]`.
    * Ejemplo: `mi_objeto[5] = 10`, o `mi_objeto["a"] = 20`, etc.
* `__delitem__`: debe eliminar al elemento asociado a la llave (o índice). Se invoca automáticamente al borrar con el operador `[]`.
    * Ejemplo: `del mi_objeto[5]`, o `del mi_objeto["a"]`, etc.
* `__contains__`: debe retornar `True` si el existe un elemento asociado a la llave (o índice) indicado. Se invoca automáticamente con `in`.
    * Ejemplo: `5 in mi_objeto`, o `"a" in mi_objeto`, etc.
