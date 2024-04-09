Conjuntos
================================================

Los `conjuntos` en Python son una estructura para simular conjuntos 
matemáticos:
* No almacenan duplicados
* Sus elementos deben ser hashables como las llaves de un diccionario
* Al igual que con las listas, sus elementos pueden ser de tipo mixto

Entre las operaciones que soportan están:
* Pertenencia: si un elemento está en un conjunto
    * Operadores: `in` y `not in`
* Subconjunto: un conjunto contiene todos los elementos de otro conjunto
    * Operadores: `<=` y `>=`
* Subconjunto propio: un conjunto es subconjunto de otro pero no son iguales
    * Operadores: `<` y `>`
* Uniones: unir los elementos de dos o más conjuntos
    * Operadores: `|`
* Intersecciones: obtener los elementos que existen en dos o más conjuntos
    * Operadores: `&`
* Diferencia: a un conjunto quitarle los elementos que también estén en otro
    * Operadores: `-`
* Diferencia simétrica: obtener los elementos que están solo en uno de dos conjuntos, pero no en los dos
    * Operadores: `^`

Sintaxis:
---------
* Para definir un conjunto es similar a las listas, solo que en lugar de usar los corchetes `[]`, en este caso se usan llaves `{}`.
* Se puede definir un conjunto vacío con `set()`.
* Se puede convertir cualquier iterable `I` a conjunto con `set(I)`, tengamos en cuenta que esto elimina los duplicados.

