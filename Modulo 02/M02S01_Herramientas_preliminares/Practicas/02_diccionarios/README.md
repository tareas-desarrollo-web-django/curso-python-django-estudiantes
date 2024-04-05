Diccionarios
================================================

Un `diccionario` en Python es una estructura de datos que sirve para almacenar parejas `llave:valor`, comunmente se dice que mapea llaves a valores.
* Es una estructura `mutable`, es decir, que se puede modificar.
* Se define poniendo las parejas `llave:valor` separados por coma entre llaves `'{}'`.
  Ejemplo: `{1:1, 2:4, 3:9, 4:16}`.
* Las `llaves` solo pueden ser objetos inmutables (o hasheables) como números, strings, o tuplas.
* Los `valores` pueden ser cualquier objeto que se pueda definir en Python.
* A pesar de ser una estructura bastante simple, es muy importante para darle legibilidad al código y también es la estructura más usada al trabajar con archivos en formato `JSON`.
* Es manejado por la clase `dict`.
* A partir de `Python 3.7`, los diccionarios respetan el orden en el que fueron insertados los elementos, por lo que al iterar sobre estos podemos esperar un orden.


Sintaxis:
---------
* Para definir un diccionario se tienen que colocar las parejas `llave:valor` separados por coma entre llaves `'{}'`:
  * `precios_productos = {'Libreta':30.90, 'Libro':43.30, 'Plumones':80.40, 'Carpetas':323.10}`
  * `nombres_productos = {2:'Libreta', 5:'Libro', 7:'Plumones', 21:'Carpetas'}`
* También se puede anidar tanto como el sistema lo permita y combinarlo con listas o lo que sea:
  * `{'categorías': [{'id':1 'nombre':'Útiles'}, {'id:3', 'nombre':'Limpieza'}]}`
* Para crear un diccionario vacío, tenemos las siguientes formas:
  * `d = {}`
  * `d = dict()`
* La clase `dict` soporta varias formas de crear un diccionario, por ejemplo dando las parejas en una lista de tuplas:
  * `precios_productos = dict([('Libreta', 30.90), ('Libro', 43.30), ('Plumones', 80.40)])`
* Para consultar el valor asignado a una llave usamos la sitaxis:
  * `precios_productos['Libreta']`
  * `nombres_productos[7]`
* Para agregar parejas de llave y valor a un diccionario, solo le asignamos un valor, si la llave ya existe entonces será actualizado, pero si no existe entonces se va a crear:
  * `precios_productos['Lápiz'] = 10.00`
  * `nombres_productos[11] = 'Lápiz'`
* Para saber si una llave ya está registrada en un diccionario, usamos el operador `in`, lo cual nos devolverá `True` si está y `False` si no está:
  * `'Libreta' in precios_productos`
  * `'5' in nombres_productos`
