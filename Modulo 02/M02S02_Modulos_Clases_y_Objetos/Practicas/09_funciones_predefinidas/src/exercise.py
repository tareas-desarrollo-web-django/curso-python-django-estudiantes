'''
Funciones predefinidas
'''


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

# class Auto:
#     def __init__(self, nombre:str, color:str, vel_max_kmh:int):
#         self.nombre = nombre
#         self.color = color
#         self.vel_max_kmh = vel_max_kmh
#         self.vel_actual = 0
    
#     def arrancar(self, vel:int):
#         if vel > self.vel_max_kmh:
#             raise ValueError(f"No se puede superar la velocidad máxima de {self.vel_max_kmh} km/h")
        
#         print(f"Arrancando el auto a {vel} km/h")
#         self.vel_actual = vel
    
#     def frenar(self):
#         print(f"Frenando el auto")
#         self.vel_actual = 0

# def sumar_numeros(a, b):
#     return a + b

# taxi = Auto("Taxi", "amarillo", 150)
# print(f"sumar_numeros es invocable? {callable(sumar_numeros)}")
# print(f"Auto es invocable? {callable(Auto)}")
# print(f"taxi es invocable? {callable(taxi)}")

# ######################################
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

# ######################################
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