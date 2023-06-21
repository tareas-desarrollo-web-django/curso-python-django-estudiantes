Múltiplos de 3
================================================

Problema
--------

Crear el archivo `src\exercise.py` e implementar en este una función con firma `multiplos_de_3(n:int)`:

* Debe devolver un conjunto con los múltiplos de 3 menores o iguales a `n`.
* `0` es múltiplo de 3.
* Asumir que `n` $\geq 0$.

Recordemos que los conjuntos de Python no respetan el orden, por lo que no hay que preocuparse por que el resultado se vea ordenado.

Validaciones
------------

Ejemplo 1:
* Entrada: `n=65`
* Salida: `{0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63}`

Ejemplo 2:
* Entrada: `n=48`
* Salida: `{0, 33, 3, 36, 6, 39, 9, 42, 12, 45, 15, 48, 18, 21, 24, 27, 30}`

Ejemplo 3:
* Entrada: `n=8`
* Salida: `{0, 3, 6}`
