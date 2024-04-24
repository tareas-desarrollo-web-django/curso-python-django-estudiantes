
##############################################################################
# Ejemplo

# class GraficaFuncion:
#     '''Clase para manejar funciones y sus graficas'''
#     def __init__(self, funcion:str, contexto):
#         # Atributos privados
#         self._f = funcion
#         self._contexto = contexto
#         # Atributos públicos
#         self.color = "negro"
#         self.visble = True

#         # De una vez preparamos el cache
#         self._preparar_cache()
    
#     def _preparar_cache(self):
#         print("Preparando el cache para acelerar el dibujado")

#     def get_f(self):
#         return self._f

#     def set_f(self, val):
#         # Primero revisamos que el valor de f sea seguro y probablemente
#         # reconstruimos el cache entre otras cosas.
#         self._f = val

#     def dibujar(self):
#         print(f"Dibujando gráfica {self._f} en {self._contexto}")


# print("*" * 40)
# x_cuadrada = GraficaFuncion("x**2", "ventana_1")
# x_cuadrada.dibujar()
# # Se puede acceder a la función e incluso modificarla
# print(f"x_cuadrada: {x_cuadrada._f}")
# x_cuadrada._f = "x**3"
# print(f"x_cuadrada: {x_cuadrada._f}")

##############################################################################
# Ejemplo

# class GraficaFuncion:
#     '''Clase para manejar funciones y sus graficas'''
#     def __init__(self, funcion:str, contexto):
#         # Atributos privados
#         self.__f = funcion
#         self.__contexto = contexto
#         # Atributos públicos
#         self.color = "negro"
#         self.visble = True

#         # De una vez preparamos el cache
#         self.__preparar_cache()
    
#     def __preparar_cache(self):
#         print("Preparando el cache para acelerar el dibujado")
    
#     def get_f(self):
#         return self.__f

#     def set_f(self, val):
#         # Primero revisamos que el valor de f sea seguro y probablemente
#         # reconstruimos el cache entre otras cosas.
#         self.__f = val

#     def dibujar(self):
#         print(f"Dibujando gráfica {self.__f} en {self.__contexto}")


# print("*" * 40)
# x_cuadrada = GraficaFuncion("x**2", "ventana_1")
# x_cuadrada.dibujar()
# # Ya no se puede acceder a la función ni incluso modificarla directamente
# print(f"x_cuadrada: {x_cuadrada.__f}")
# x_cuadrada.__f = "x**3"
# print(f"x_cuadrada: {x_cuadrada.__f}")
# # Solo se puede mediante los getters y setters
# print(f"x_cuadrada: {x_cuadrada.get_f()}")
# x_cuadrada.set_f("x**3")
# print(f"x_cuadrada: {x_cuadrada.get_f()}")

##############################################################################
