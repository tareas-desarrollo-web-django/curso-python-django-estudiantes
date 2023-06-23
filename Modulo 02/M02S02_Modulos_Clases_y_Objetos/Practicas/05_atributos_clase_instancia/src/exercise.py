'''
Atributos de clase y atributos de instancia
================================================

Los atributos de instancia son aquellos que pertenecen a cada instancia en particular.
* Estos van declarados dentro del constructor.
* Solo pueden ser consultados por la instancia misma.

Los atributos de clase son aquellos que pertenecen a la clase.
* Estos van declarados fuera del constructor.
* Solo se pueden modificar desde la clase misma.
* Si se intenta modificar un atributo de clase desde una instancia, entonces se creará un atributo de instancia solo para la instancia en cuestión.
* Pueden ser consultados por la clase misma y por las instancias, siempre que la instancia no tengan ya un atributo con el mismo nombre.
    * Al consultar un atributo desde una instancia primero se revisa la instancia, si no hay un atributo con ese nombre en la instancia entonces se busca en la clase.
'''

##############################################################################
# Atributos de clase

# # Clase con puros atributos de clase
# class Auto:
#     llantas = 4
#     color = "Rojo"
#     vel_max_kmh = 200

# # Generamos dos instancias de la clase Auto
# taxi = Auto()
# deportivo = Auto()
# bus = Auto()

# # Mostramos los atributos
# print("*" * 40)
# print("Atributos iniciales")
# print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
# print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}")
# print(f"{bus.color=}, {bus.llantas=}, {bus.vel_max_kmh=}\n")

# # Modificamos los atributos desde el objeto 'deportivo'
# # Esto en realidad genera atributos de instancia para el objeto 'deportivo'
# print("*" * 40)
# deportivo.color = "Naranja"
# deportivo.vel_max_kmh = 400

# # Mostramos los atributos después de la modificación desde 'deportivo'
# # Y vemos que solo el objeto 'deportivo' cambió
# print("Atributos modificados desde deportivo")
# print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
# print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}")
# print(f"{bus.color=}, {bus.llantas=}, {bus.vel_max_kmh=}\n")

# # Ahora modificamos atributos desde la clase
# print("*" * 40)
# Auto.llantas = 8
# Auto.color = "Negro"

# # Mostramos los atributos después de la modificación desde la clase
# # Y vemos que solo taxi y bus parecen haber cambiado, pero en realidad
# # taxi y bus como no tienen los atributos especificados entonces muestran los
# # atributos de la clase
# print("Atributos modificados desde la clase")
# print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
# print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}")
# print(f"{bus.color=}, {bus.llantas=}, {bus.vel_max_kmh=}\n")

##############################################################################
# Atributos de instancia

# Clase con puros atributos de instancia
class Automovil:
    def __init__(self):
        self.llantas = 4
        self.color = "Rojo"
        self.vel_max_kmh = 200


# Generamos dos instancias de la clase Automovil
taxi = Automovil()
deportivo = Automovil()
bus = Automovil()

# Mostramos los atributos
print("*" * 40)
print("Atributos iniciales")
print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}")
print(f"{bus.color=}, {bus.llantas=}, {bus.vel_max_kmh=}\n")

# Modificamos los atributos desde el objeto 'deportivo'
# Esto en realidad genera atributos de instancia para el objeto 'deportivo'
print("*" * 40)
deportivo.color = "Naranja"
deportivo.vel_max_kmh = 400
# Mostramos los atributos después de la modificación desde 'deportivo'
# Y vemos que solo el objeto 'deportivo' cambió
print("Atributos modificados desde deportivo")
print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}")
print(f"{bus.color=}, {bus.llantas=}, {bus.vel_max_kmh=}\n")

# Ahora modificamos atributos desde la clase
# Como la clase no tiene atributos en esta ocación, lo que ocurrirá es que
# los atributos se agregarán a la clase como atributos de clase
print("*" * 40)
Automovil.llantas = 8
Automovil.color = "Negro"
# Mostramos los atributos después de la modificación desde la clase
# Y vemos que nada cambió
print("Atributos modificados desde la clase")
print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}")
print(f"{bus.color=}, {bus.llantas=}, {bus.vel_max_kmh=}\n")

# Pero si eliminamos el atributo 'llantas' de taxi, vemos que la próxima vez 
# que lo consultemos como la clase ahora tiene un atributo llamado 'llantas',
# entonces obtendremos el valor del atributo de la clase
print("*" * 40)
print(f"Antes de eliminar llantas de taxe: {taxi.llantas = }")
del taxi.llantas
print(f"Antes de eliminar llantas de taxe: {taxi.llantas = }")

##############################################################################