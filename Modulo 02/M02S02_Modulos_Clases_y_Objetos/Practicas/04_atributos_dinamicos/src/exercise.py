'''
Atributos dinámicos de objetos
================================

Python tiene una libertad muy grande al implementar código. Un ejemplo de esto es que a los objetos se les puede agregar y borrar atributos dinámicamente, similar a los diccionarios.

Esto aplica también a las clases, ya que, por mas extraño que parezca, las clases también son objetos, es por eso que pueden tener atributos.


Sintaxis:
----------

* Para agregar un atributo a un objeto, solo basta con asignarle un valor, cuando Python nota que no existe, entonces lo crea solo para el objeto en cuestión.
    * Ejemplo: `MiObjeto.nuevo_atributo = 10`
* Para eliminar un atributo de un objeto, usamos la palabra `del`.
    * Ejemplo: `del MiObjeto.nuevo_atributo`.
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

# Función auxiliar para mostrar los atributos de un objeto Auto
def print_atributos(obj):
    print(f"{obj.nombre}:" if hasattr(obj, "nombre") else "Desconocido: ")

    for k,v in vars(obj).items():
        if k == "nombre":
            continue
        print(f"\t{k}:{v}")

##############################################################################
# Operaciones

# Creamos un Auto llamado Taxi.
taxi = Auto("Taxi", "Amarillo", 150)
deportivo = Auto("Deportivo", "Amarillo", 150)

# Mostramos los atributos actuales de los objetos
# Vemos que el atributo de clase 'llantas' no se muestra porque no pertenece
# a las instancias
print("*" * 40)
print("Atributos originales")
print_atributos(taxi)
print_atributos(deportivo)

# Agregamos un atributo al objeto taxi y mostramos los atributos de los objetos
taxi.cilindros = 4
print("*" * 40)
print("Despues de agregar atributos a Taxi")
print_atributos(taxi)
print_atributos(deportivo)

# Borramos atributos de taxi y mostramos los atributos de los objetos
del taxi.color
print("*" * 40)
print("Despues de borrar atributos a Taxi")
print_atributos(taxi)
print_atributos(deportivo)

# # Al referenciar un atributo sobre una instancia, primero se revisa si
# # existe en la instancia, si no entonces busca en la clase,
# # es por eso que podemos consultar el atributo 'llantas' desde las instancias
# print("*" * 40)
# print("Consultamos atributos de clase desde las instancias")
# print(f"{taxi.llantas=}")
# print(f"{deportivo.llantas=}")
# print(f"{Auto.llantas=}\n")

# # Por eso al modificar el atributo de clase, pareciera que se modificó
# # en todas las instancias, pero la realidad es que las instancias solo muestran
# # el valor del atributo de la clase
# Auto.llantas = 8
# print("Atributo de clase despues de ser modificado")
# print(f"{taxi.llantas=}")
# print(f"{deportivo.llantas=}")
# print(f"{Auto.llantas=}\n")

# # También podemos agregar atributos a la clase
# Auto.puertas = 4
# print("*" * 40)
# print("Agregamos un atributo a la clase")
# print(f"{taxi.puertas=}")
# print(f"{deportivo.puertas=}")
# print(f"{Auto.puertas=}")

##############################################################################