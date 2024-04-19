
##############################################################################

class BaseDatos:
    def __init__(self):
        print("Conectado a la base de datos.")
    
    def __del__(self):
        print("Conexión liberada.")


print("*" * 40)
# Creamos un objeto
conexion = BaseDatos()
# Lo eliminamos, y como es la única referencia al objeto, el destructor debería ejecutarse
# del conexion

##############################################################################

# print("*" * 40)

# # Clase que lleva el conteo de cuantas instancias de esta hay activas
# class Auto:
#     instancias = 0

#     def __init__(self, velocidad, color):
#         self.velocidad = velocidad
#         self.color = color
        
#         # Agregamos una instancia al contador
#         self.__class__.instancias += 1
#         print("Auto creado")
    
#     def __del__(self):
#         # Restamos una instancia al contador
#         self.__class__.instancias -= 1
#         print("Auto eliminado")


# # Creamos objetos
# print(f"Autos activos: {Auto.instancias}")
# deportivo = Auto(velocidad=400, color="rojo")
# print(f"Autos activos: {Auto.instancias}")
# taxi = Auto(velocidad=150, color="amarillo")
# print(f"Autos activos: {Auto.instancias}")
# bus = Auto(velocidad=100, color="azul")
# print(f"Autos activos: {Auto.instancias}\n")

# # Eliminamos objetos
# del deportivo
# print(f"Autos activos: {Auto.instancias}")
# del taxi
# print(f"Autos activos: {Auto.instancias}")
# del bus
# print(f"Autos activos: {Auto.instancias}")

##############################################################################