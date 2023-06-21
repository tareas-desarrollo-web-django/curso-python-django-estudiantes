Desempaquetado de valores y de parámetros
================================================

Python tiene un mecanismo que simplifica el manejo de valores contenidos en una lista o tupla:
* El mecanismo consiste en separar los valores de una lista o tupla de manera muy sencilla

Sintaxis:
----------

* Podemos asignar los valores de una lista a variables con: `var1, var2, ..., varN = lista`
    * En este caso el número de variables debe ser igual a los elementos en la lista
* Si queremos separar solo los primeros valores y el resto dejarlos en una lista: `var1, var2, ..., vark, *restante = lista`
    * Así los primeros `k` valores serán asignados a las primeras variables, y el resto de elementos será asignado a una lista cuyo nombre debe estar al final precedido por un arterisco `*`.
* Para desempaquetar los valores de una lista y usarlos como parámetros separados de una función: `funcion(*lista)`
    * Así cada elemento de la lista se enviará como parámetro a la función en en mismo orden en el que están en la lista.
