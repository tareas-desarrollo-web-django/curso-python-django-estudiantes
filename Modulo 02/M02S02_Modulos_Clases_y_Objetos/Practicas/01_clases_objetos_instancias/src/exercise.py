'''
Clases, objetos e instancias
================================================

En Python, una ***Clase*** es un segmento encapsulado de códido, que describe las características, funciones e interacciones de un objeto.

Un ***Objeto*** es un elemento de código creado a partir de una clase. Cuando creamos un objeto desde una clase, también se dice que el objeto es una ***Instancia*** de la clase.

Los ***atributos*** son variables que están ligadas a objetos, y son usados para almacenar datos esenciales para el funcionamiento de las instancias. Pueden verse como datos o como características del objeto.

Sintaxis:
----------

* Para definir una clase se usa la sintaxis `class NombreDeClase:`.
    * Ejemplo: `class MiClase:`.
* Dentro de la clase se pueden definir variables, funciones, etc. Lo cual veremos más adelante.
* Para crear una instancia de la clase se invoca en nombre de la clase como si fuera una función.
    * Ejemplo: `mi_objeto = MiClase()`
* Para saber si un objeto es una instacia de una clase podemos usar la función predefinida `isinstance`.
    * Ejemplo: `isinstance(5, int)` que resulta en `True`.
* También podemos revisar si un objeto es una instancia de al menos una de varias clases usando el operador de unión `|`.
    * Ejemplo: `isinstance("3.23", float|str)` o `isinstance(3.23, float|str)`, ambas resultan `True`.
* Una clase en sí es un nuevo tipo de dato, por lo que podemos consultar el tipo de dato de un objeto con la función predefinida `type`.
    * Ejemplo: `type("hola")` resulta en `<class 'str'>`.
* Para saber el nombre de una clase usamos el atributo mágico `__name__` sobre la clase.
    * Ejemplo: `MiClase.__name__`
* Para obtener la clase de la cual es instancia un objeto usamos el atributo mágico `__class__`, pero esta vez sobre el objeto, no sobre la clase.
    * Ejemplo: `mi_objeto.__class__`
'''

##############################################################################
# Definiciones

# Clase con atributos predefinidos
class Auto:
    llantas = 4
    color = "Rojo"
    vel_max_kmh = 200


# Generamos dos instancias de la clase Auto
taxi = Auto()
deportivo = Auto()

##############################################################################
# Operaciones

# Mostramos los atributos
print("Atributos iniciales")
print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}\n")

# Cambiamos algunos valores de los atributos
deportivo.vel_max_kmh = 400
deportivo.color = "Naranja"

# Volvemos a mostrar los atributos
print("Atributos modificados")
print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}\n")

# Revisamos si algunos objetos son instancias de la clase Auto
print(f"taxi es Auto: {isinstance(taxi, Auto)}")
print(f"deportivo es Auto: {isinstance(deportivo, Auto)}")
print(f"str es Auto: {isinstance(str, Auto)}\n")

# Consultamos el tipo de dato de un objeto Auto
print(f"{type(taxi)=}")
# Obtenemos el nombre de la clase Auto
print(f"Nombre de clase Auto: {Auto.__name__}\n")

# Obtenemos el objeto clase a la que pertenece taxi
# No es el nombre, sino la clase en sí
print(f"Clase de taxi: {taxi.__class__}")
# Podemos saber el nombre de la calse a la que pertenece taxi
print(f"Nombre de clase de taxi: {taxi.__class__.__name__}\n")

# Podemos crear un objeto Auto accediendo a la clase a través de taxi
bus = taxi.__class__()
# Mostramos los atributos iniciales de bus
print(f"{bus.color=}, {bus.llantas=}, {bus.vel_max_kmh=}\n")

##############################################################################

