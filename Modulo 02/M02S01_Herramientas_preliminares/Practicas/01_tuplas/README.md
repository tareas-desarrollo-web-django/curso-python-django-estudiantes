Tuplas
================================================

Una `tupla` en Python es una estructura que sirve para almacenar una colección de datos de cualquier tipo, similar a una `lista`, pero con las siguientes características:
* Es una estructura `inmutable`, es decir, que no se puede modificar ni agregarle elementos.
* Se define usando paréntesis. Ejemplo `(1, "Libro", True)`.
* Son útiles cuando queremos prevenir que alguna función modifique la colección de elementos.
* Son más eficientes que las listas ya que al no poder cambiar, Python puede optimizar su rendimiento.
* Se pueden usar como llaves de un diccionario, lo cual no es posible con listas.
* Es manejada por la clase `tuple`.

Una consideración especial es que solo almacena las referencias de los objetos, por lo que dichas referencias son lo que no puede modificarse, pero el contenido de los objetos sí. 
Por ejemplo, en la tupla `("elementos", [1, 4])`, estamos incluyendo un objeto de lista, por lo que no podemos poner en su lugar otra lista en sí, pero lo que sí podemos hacer es modificarla.


Sintaxis:
---------
* Para definir una lista se tienen que colocar sus elementos entre paréntesis separados por coma `'()'`:
  * `precios = (30.90, 43.30, 80.40, 323.10)`
  * `productos = ('Libro', 'Libreta', 'Lápiz', 'Plumón')`
* Como cualquier estructura, se pueden anidar tanto como lo permita el sistema:
  * `filas = ((1, 5, 7, 3), (1, 5, 76, 7), (9, 3, 6, 8))`
* El uso de paréntesis es muy general en Python, por ejemplo, se usa para envolver expresiones, por ejemplo `x * (a + 3)`, incluso `(5)` es una expresión. Por lo tanto, si queremos definir una lista que solo contiene un elmento, tenemos que incluir una coma después de dicho elemento, para que Python entienda que no se trata de una expresión:
  * `I = (3,)`
* Si queremos definir una lista vacía, tenemos que usar el constructor de la clase `'tuple'`:
  * `v = tuple()`
* La clase `tuple` también sirve para crear tuplas a partir de otros iterables como listas:
  * `v = tuple([1, 2, 4])`

