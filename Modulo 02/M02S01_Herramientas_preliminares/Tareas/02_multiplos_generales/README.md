Múltiplos generales
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una función con firma `multiplos(k:int, n:int)`:

* Debe retornar un conjunto con los múltiplos de `k` menores o iguales a `n`
* `0` es múltiplo de `k`.
* Asumir que `k` $> 0$, `n` $\geq 0$

Recordemos que los conjuntos de Python no respetan el orden, por lo que no hay que preocuparse por que el resultado se vea ordenado.


Validaciones
------------

Ejemplo 1:
* Entrada: `k=17, n=65`
* Salida: `{0, 17, 34, 51}`

Ejemplo 2:
* Entrada: `k=20, n=60`
* Salida: `{0, 40, 20, 60}`

Ejemplo 3:
* Entrada: `k=34, n=157`
* Salida: `{0, 34, 68, 102, 136}`