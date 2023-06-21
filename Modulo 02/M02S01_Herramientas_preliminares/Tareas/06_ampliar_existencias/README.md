Ampliar existencia de productos
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `agregar_existencias(ids:list[str])`:

* Recibe una lista de textos los cuales representan ID de productos. Estos productos serán agregados a la lista de productos en existencia.
* La lista actual de ID de productos que están en existencia es:
    * `["a_1", "a_2", "a_3", "b_1", "b_2", "b_4", "b_5", "b_8", "c_3", "c_7", "c_9", "c_10", "c_11", "d_2", "d_3", "d_6", "d_8", "d_9", "d_23", "d_35"]`
* Debe regresar una lista sin repeticiones de los ID de productos en existencia actualizados, agregando los productos recibidos.
* La lista debe estar ordenada de menor a mayor, alfabéticamente (usar la función `sorted`).

Validaciones
------------

Ejemplo 1:
* Entrada: `['c_27', 'a_27', 'c_35', 'c_16', 'a_7', 'd_33', 'a_43', 'b_43', 'c_24', 'c_7', 'd_21', 'a_38']`
* Salida: `['a_1', 'a_2', 'a_27', 'a_3', 'a_38', 'a_43', 'a_7', 'b_1', 'b_2', 'b_4', 'b_43', 'b_5', 'b_8', 'c_10', 'c_11', 'c_16', 'c_24', 'c_27', 'c_3', 'c_35', 'c_7', 'c_9', 'd_2', 'd_21', 'd_23', 'd_3', 'd_33', 'd_35', 'd_6', 'd_8', 'd_9']`

Ejemplo 2:
* Entrada: `['b_26', 'd_45', 'b_31', 'a_8', 'd_33', 'a_15', 'c_35', 'd_45']`
* Salida: `['a_1', 'a_15', 'a_2', 'a_3', 'a_8', 'b_1', 'b_2', 'b_26', 'b_31', 'b_4', 'b_5', 'b_8', 'c_10', 'c_11', 'c_3', 'c_35', 'c_7', 'c_9', 'd_2', 'd_23', 'd_3', 'd_33', 'd_35', 'd_45', 'd_6', 'd_8', 'd_9']`

Ejemplo 3:
* Entrada: `['a_32', 'a_37', 'a_3', 'b_36', 'c_34']`
* Salida: `['a_1', 'a_2', 'a_3', 'a_32', 'a_37', 'b_1', 'b_2', 'b_36', 'b_4', 'b_5', 'b_8', 'c_10', 'c_11', 'c_3', 'c_34', 'c_7', 'c_9', 'd_2', 'd_23', 'd_3', 'd_35', 'd_6', 'd_8', 'd_9']`
