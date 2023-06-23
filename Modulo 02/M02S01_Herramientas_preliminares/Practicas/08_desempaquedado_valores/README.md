Desempaquetado de valores y de parámetros
================================================

Python tiene un mecanismo que simplifica el manejo de valores contenidos en una lista o tupla, llamado `desempaquetado de valores`:
* Consiste en separar los valores de un iterable en diferentes variables.
* Soporta un bune nivel de generalización.
* Es muy útil tanto para nombrar los valores de un iterable, como para enviar parámetros a las funciones.
* Para el caso de los parámetros, también tiene soporte para diccionarios.

Sintaxis:
----------

* Podemos asignar los valores de una lista a variables con:
    * ```python
      var1, var2, ..., varN = lista
      ```
* Si dejar un subconjunto de los valores en una lista:
    * ```python
      *restante, var1, var2, var3 = lista
      var1, var2, *restante, var3 = lista
      var1, var2, var3, *restante = lista
      ```
* Para desempaquetar los valores de una lista y usarlos como parámetros separados de una función: 
    * ```python
      mi_funcion(*lista_de_argumentos)
      ```
      Los argumentos se envían separados en el mimso orden de la lista.
    * ```python
      mi_funcion(**diccionario_de_argumentos)
      ```
      Los argumentos se envían en concordancia con las llaves del diccionario.
