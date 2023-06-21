Consultar existencia de productos
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una función con firma `existencias(ids:list[str])`:

* Recibe una lista de textos los cuales representan ID de productos.
* Debe regresar una lista sin repeticiones de los ID de productos enviados que sí están en existencia.
* La lista debe estar ordenada de menor a mayor alfabéticamente (usar la función `sorted`).
* La lista completa de ID de productos que están en existencia es:
    * `["a_1", "a_2", "a_3", "b_1", "b_2", "b_4", "b_5", "b_8", "c_3", "c_7", "c_9", "c_10", "c_11", "d_2", "d_3", "d_6", "d_8", "d_9", "d_23", "d_35"]`

Validaciones
------------

Ejemplo 1:
* Entrada: `['a_41', 'd_32', 'a_34', 'd_3', 'd_4', 'a_43', 'd_12', 'd_2', 'b_0', 'c_39', 'd_2', 'd_43', 'd_8', 'c_46']`
* Salida: `['d_2', 'd_3', 'd_8']`

Ejemplo 2:
* Entrada: `['a_16', 'd_29', 'c_6', 'a_30', 'd_22', 'a_24', 'c_23', 'a_43', 'd_21']`
* Salida: `[]`

Ejemplo 3:
* Entrada: `['d_1', 'b_41', 'a_3', 'c_48', 'b_3', 'b_5', 'b_28', 'a_15', 'b_14', 'd_21', 'b_25', 'a_41', 'd_8', 'd_10', 'd_37', 'b_20', 'b_22', 'b_23', 'd_47', 'a_32', 'c_28', 'a_46', 'a_6', 'a_8', 'a_37', 'c_43']`
* Salida: `['a_3', 'b_5', 'd_8']`
