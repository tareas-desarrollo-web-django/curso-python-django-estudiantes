'''
Clases, objetos e instancias
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

