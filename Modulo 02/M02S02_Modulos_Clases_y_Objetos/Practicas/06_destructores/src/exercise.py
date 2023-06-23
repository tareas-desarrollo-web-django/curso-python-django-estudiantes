'''
Destructores de clase
=======================

El ***destructor*** es una método especial que siempre se ejecuta cuando una instancia de dicha clase es eliminada.
* Generalmente se usa para liberar los recursos usados por el objeto, aunque no se limita a esto.

Sintaxis:
----------

* El destructor es un método que debe estar definido dentro de una clase y cuya firma es `def __del__(self):`.
'''

##############################################################################
# Definiciones

# class BaseDatos:
#     def __init__(self):
#         print("Conectado a la base de datos.")
    
#     def __del__(self):
#         print("Conexión liberada.")


# print("*" * 40)
# del conexion

##############################################################################
# Ejemplos de uso
print("*" * 40)

# Clase que lleva el conteo de cuantas instancias de esta hay activas
class Auto:
    instancias = 0

    def __init__(self, velocidad, color):
        self.velocidad = velocidad
        self.color = color
        
        # Agregamos una instancia al contador
        self.__class__.instancias += 1
        print("Auto creado")
    
    def __del__(self):
        # Restamos una instancia al contador
        self.__class__.instancias -= 1
        print("Auto eliminado")


# Creamos objetos
print(f"Autos activos: {Auto.instancias}")
deportivo = Auto(velocidad=400, color="rojo")
print(f"Autos activos: {Auto.instancias}")
taxi = Auto(velocidad=150, color="amarillo")
print(f"Autos activos: {Auto.instancias}")
bus = Auto(velocidad=100, color="azul")
print(f"Autos activos: {Auto.instancias}\n")

# Eliminamos objetos
del deportivo
print(f"Autos activos: {Auto.instancias}")
del taxi
print(f"Autos activos: {Auto.instancias}")
del bus
print(f"Autos activos: {Auto.instancias}")

##############################################################################