'''
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
'''

##############################################################################
# Definiciones

class Auto:
    def __init__(self, nombre:str, color:str, vel_max_kmh:int):
        self.nombre = nombre
        self.color = color
        self.vel_max_kmh = vel_max_kmh
        self.vel_actual = 0
    
    def arrancar(self, vel:int):
        if vel > self.vel_max_kmh:
            raise ValueError(f"No se puede superar la velocidad máxima de {self.vel_max_kmh} km/h")
        
        print(f"Arrancando el auto a {vel} km/h")
        self.vel_actual = vel
    
    def frenar(self):
        print(f"Frenando el auto")
        self.vel_actual = 0




##############################################################################
# # Ejemplo
# print("*" * 40)

# numeros = [1, 2, 5, 6, 8, -1]
# son_positivos = all([n >= 0 for n in numeros])
# print(f"Números: {numeros}")
# print(f"Todos son positivos? {son_positivos}")

# numeros = [1, 2, 5, 6, 8, 1]
# son_positivos = all([n >= 0 for n in numeros])
# print(f"Números: {numeros}")
# print(f"Todos son positivos? {son_positivos}")

# ##############################################################################
# # Ejemplo
# print("*" * 40)

# numeros = [1, 2, 5, 6, 8, -1]
# alguno_negativo = any([n < 0 for n in numeros])
# print(f"Números: {numeros}")
# print(f"Alguno es negativo? {alguno_negativo}")

# numeros = [1, 2, 5, 6, 8, 1]
# alguno_negativo = any([n < 0 for n in numeros])
# print(f"Números: {numeros}")
# print(f"Alguno es negativo? {alguno_negativo}")

# ##############################################################################
# # Ejemplo
# print("*" * 40)

# def sumar_numeros(a, b):
#     return a + b

# taxi = Auto("Taxi", "amarillo", 150)
# print(f"sumar_numeros es invocable? {callable(sumar_numeros)}")
# print(f"Auto es invocable? {callable(Auto)}")
# print(f"taxi es invocable? {callable(taxi)}")

# ##############################################################################
# # Ejemplo
# print("*" * 40)

# bus = Auto("Bus", "azul", 100)
# print(f"Bus tiene color? {hasattr(bus, 'color')}")
# print(f"El color del bus es: {getattr(bus, 'color')}")
# setattr(bus, "color", "verde")
# print(f"El nuevo color del bus es: {bus.color}")
# delattr(bus, "color")
# print(f"Bus tiene color? {hasattr(bus, 'color')}")
# # También podemos invocar sus funciones
# getattr(bus, "arrancar")(100)

# ##############################################################################
# # Ejemplo
# print("*" * 40)

# deportivo = Auto("Deportivo", "naranja", 400)
# print("Los atributos de 'deportivo' son:")
# print(dir(deportivo))

# ##############################################################################
# # Ejemplo
# print("*" * 40)

# menu = ["Guardar", "Borrar", "Mover", "Salir"]
# print(f"Menú enumerado desde 0: {list(enumerate(menu))}")

# print("Opciones de menú:")
# for i, opcion in enumerate(menu, 1):
#     print(f"{i}.- {opcion}")

# ##############################################################################
# # Ejemplo
# print("*" * 40)

# productos = ["ssd", "ram", "cpu", "teclado"]
# precios = [2500, 1000, 4500, 800]

# print("Unidos horizontalmente:")
# print(list(zip(productos, precios)))

# print("Catálogo:")
# for prod, precio in zip(productos, precios):
#     print(f"* {prod} - ${precio}")

# ##############################################################################