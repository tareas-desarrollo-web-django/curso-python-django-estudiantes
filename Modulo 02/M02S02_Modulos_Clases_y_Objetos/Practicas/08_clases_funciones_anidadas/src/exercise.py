'''
Clases y funciones anidadas
'''

##############################################################################
# Ejemplo

# # Dentro definimos una función la cual no puede ser accedida desde fuera
# def ordenar_por_longitud(datos):
#     def longitud(s):
#         '''Calcula la longitud del texto 's', regresa 0 si es None'''
#         if s is None:
#             return 0
#         return len(s)
    
#     return sorted(datos, key=longitud)

# claves = ["tincidunt", "Quisque", None, "lacus", "egestas", "tincidunt",
#          "placerat", "quis", "lacinia", None, "vulputate", "finibus", 
#          "aliquet", "ste", "Pellentesque", "efficitur", "z"]
# claves_ordenadas = ordenar_por_longitud(claves)
# print(f"Claves ordenadas: {claves_ordenadas}")

##############################################################################
# Ejemplo

# # Función que contiene una clase la cual no puede ser accedida desde fuera
# # Solo esta función puede generar instancias de dicha clase
# def generar_escalador(k):
#     class Escalador:
#         '''
#         Clase que se construye con un número 'k' y ese número se puede
#         multiplicar por otros con el método 'por'.
#         '''
#         def __init__(self, k):
#             self.k = k
#         def por(self, n):
#             return self.k * n
    
#     # Construye un objeto Escalador con el valor (k) y lo retorna
#     return Escalador(k)


# # Fabricamos un escalador de 5
# cinco = generar_escalador(5)
# print(f"5 * 10 = {cinco.por(10)}")

##############################################################################