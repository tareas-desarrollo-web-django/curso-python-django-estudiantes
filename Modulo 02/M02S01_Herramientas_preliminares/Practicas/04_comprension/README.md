Iterables (listas, conjuntos, diccionarios, etc) por comprensión
=================================================================

Generar iterables por comprensión consiste usar un iterable base para generar otro iterable:
* La idea es tomar el iterable base para crear otro iterable, donde a cada elemento del iterable base se le aplicará una transformación a través de una expresión de Python.
* El iterable resultante no tiene que ser del mismo tipo que el base, es decir, podemos crear una lista a partir de una tupla, o un diccionario a partir de una lista, etc.
* Se le puede aplicar un filtro a la comprensión para solo quedarnos con los elementos que satisfagan las condiciones del filtro

Sintaxis:
---------
* La estructura básica de una comprensión es: `expresion for var in iterable_base`
    * Ejemplo: `[2 * i + 1 for i in range(10)]`
* La estructura agregando un filtro es: `expresion for var in iterable_base if condicion`
    * Ejemplo: `[i for i in range(10) if i % 2 == 0]`
* La estructura de una comprensión con dos iterables base anidados es: `expresion for var1 in iterable_base_1 for var2 in iterable_base_2`
    * Ejemplo: `[(i, j) for i in range(3) for j in range(3)]`


