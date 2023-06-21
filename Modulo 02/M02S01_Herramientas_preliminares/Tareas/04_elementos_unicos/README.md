Elementos únicos
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una función con firma `unicos(list[int])`:

* Recibe una lista de enteros.
* Debe retornar una lista de enteros, la cual contenga los elementos únicos que aparecen en la lista recibida.
* La lista debe estar ordenada de menor a mayor (usar la función `sorted`).

Validaciones
------------

Ejemplo 1:
* Entrada: `[16, 16, 13, 14, 19, 17, 11, 16, 14, 15, 10, 15, 10, 14, 20]`
* Salida: `[10, 11, 13, 14, 15, 16, 17, 19, 20]`

Ejemplo 2:
* Entrada: `[20, 1, 2, 12, 11, 20, 16, 9, 16, 8, 5, 5, 1, 3, 7]`
* Salida: `[1, 2, 3, 5, 7, 8, 9, 11, 12, 16, 20]`

Ejemplo 3:
* Entrada: `[8, 7, 10, 16, 2, 1, 7, 12, 1, 12, 3, 2, 2, 8, 1, 13, 9, 16, 18, 15]`
* Salida: `[1, 2, 3, 7, 8, 9, 10, 12, 13, 15, 16, 18]`