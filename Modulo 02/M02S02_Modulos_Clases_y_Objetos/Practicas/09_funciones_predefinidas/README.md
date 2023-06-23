Funciones predefinidas
=======================

Python incluye una lista de funciones predefinidas o ***Built-in functions***.

* La lista es muy extensa, pero son funciones con mucho potencial.
* La lista completa la pueden encontrar en https://docs.python.org/es/3/library/functions.html.
* Son funciones globales que se pueden usar en cualquier lugar de nuestro código.

Sintaxis:
----------

Algunas de la funciones predefinidas están listadas a continuación:

* `abs(n)`: devuelve el valor absoluto de un número
* `all(iterable)`: recibe un iterable de valores booleanos y devuelve `True` si todos los valores son `True`.
* `any(iterable)`: recibe un iterable de valores booleanos y devuelve `True` si al menos uno de los valores es `True`.
* `callable(obj)`: recibe un objeto y devuelve `True` si el objeto es invocable con `()`.
* `delattr(obj, attr)`: elimina un atributo del objeto.
* `getattr(obj, attr)`: obtiene un atributo del objeto.
* `hasattr(obj, attr)`: devuelve `True` si el objeto contiene el atributo.
* `setattr(obj, attr, val)`: asigna un valor a un atributo del objeto.
* `dir(obj)`: devuelve la lista de atributos del objeto
* `enumerate(iterable)`: enumera los elementos del iterable comenzando desde el cero, aunque puede especificarse el inicio de la enumeración.
* `input(msg)`: lee una linea de la entrada, mostrando un mensaje.
* `isinstance(obj, clases)`: revisa si el objeto es instancia de alguna de las clases especificadas.
* `issubclass(cls, clases)`: revisa si la clase es subclase de alguna de las clases especificadas.
* `map(func, iterable)`: aplica una función a los elementos de un iterable.
* `max(...)`: devuelve el máximo valor encontrado en una lista de valores, los valores pueden ser dados en un único iterable o como parámetros separados.
* `min(...)`: devuelve el mínimo valor encontrado en una lista de valores, los valores pueden ser dados en un único iterable o como parámetros separados.
* `sorted(iterable)`: devuelve una copia ordenadad del iterable, en forma de lista.
* `sum(iterable)`: suma los elementos de un iterable.
* `type(obj)`: devuelve el tipo de dato del objeto.
* `zip(iterable1, iterable2, ...)`: une horizontalmente los iterables, todos deben ser del mismo tamaño. Devuelve tuplas donde la primera contiene todos los primeros elementos de cada iterable, la segunda tupla contiene todos los segundos elementos de los iterables, etc.