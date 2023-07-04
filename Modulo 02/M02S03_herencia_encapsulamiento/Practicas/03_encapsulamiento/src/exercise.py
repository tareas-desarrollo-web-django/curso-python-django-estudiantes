'''
Encapsulamiento
=================

En Python, el ***encapsulamiento*** se refiere al mecanismo de proteger los atributos de una clase, de modo que solo la clase pueda usarlos y que además pueda proveer métodos para manipularlos de manera segura (getters y setters).
* Esto se lleva a cabo mediante atributos privados o atributos protegidos.
* Este mecanismo no es del todo real en sí, si no más bien una convención entre la comunidad de Python.

Sintaxis:
----------
* Los atributos (métodos) privados se definen con un guión bajo precediendo el nombre del atributo. Por ejemplo `self._num_pedidos`.
    * Es importante remarcar que esto solo es una convención entre la comunidad de programadores de Python, ya que eso no impide el acceso y modificación de dichos atributos.
    * La idea es respetar esta convención y nunca consultar ni modificar atributos que comiencen con un `'_'`, aunque en realidad sí es posible hacerlo.
* Los atributos (métodos) protegidos se definen con dos guiones bajos precediendo el nombre del atributo. Por ejemplo `self.__num_pedidos`.
    * En este caso ya no es posible acceder ni modificar directamente el atributo con ese nombre.
    * La realidad es que Python cambia el nombre del atributo en todos los lugares donde aparece, pero solo dentro del cuerpo de la clase.
    * El atributo sigue existiendo, pero con un nombre un poco diferente.
    * Incluso sabiendo eso, es importante respetar el atributo y no acceder a este desde fuera de la clase usando su nombre alterado.
    * El objetivo de este mecanismo solo es proteger el atributo, para que sea muy poco probable que al heredar a una subclase, vaya a haber problemas si se define otro atributo con el mismo nombre en la subclase.
'''

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
# Ya no se puede acceder a la función ni incluso modificarla directamente
# print(f"x_cuadrada: {x_cuadrada.__f}")
# x_cuadrada.__f = "x**3"
# print(f"x_cuadrada: {x_cuadrada.__f}")
# Solo se puede mediante los getters y setters
# print(f"x_cuadrada: {x_cuadrada.get_f()}")
# x_cuadrada.set_f("x**3")
# print(f"x_cuadrada: {x_cuadrada.get_f()}")

##############################################################################
