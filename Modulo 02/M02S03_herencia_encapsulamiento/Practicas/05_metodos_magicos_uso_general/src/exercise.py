'''
Métodos dunder (mágicos) de uso general
=============================================

La forma en la que Python incorpora sobrecarga de operadores es a través de métodos especiales llamados ***dunder*** o ***mágicos***. Dunder viene de combinar las palabas **d**ouble-**under**score, ya que los métodos mágicos inician y terminan don doble guión bajo.

Sintaxis:
----------

Aquí veremos los métodos mágicos de uso general:
* `__str__`: este método debe regresar un texto que describa de manera amigable el objeto y su contenido. Es lo que se muestra al invocar `print` sobre el objeto.
* `__repr__`: lo ideal es que este método regrese un texto que se vea como una expresión válida de Python que se pueda usar para recrear el objeto. Si no es posible, entonces debe regresar información útil del objeto de la forma `<... informacion del objeto ...>`.
* `__call__`: si se implementa este método en una clase, entonces todas sus instancias podrán ser invocables como si fueran funciones, y esta es la función que se ejecutará cuando el objeto se invoque.
'''

##############################################################################
# Ejemplo

# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# print("*" * 40)
# print("Sin definir __str__ ni __repr__:")
# p = Punto(3,5)
# q = Punto(1,8)
# print("print")
# print("p =", p)
# print("q =", q)
# print("str")
# print("p =", str(p))
# print("q =", str(q))
# print("repr")
# print("p =", repr(p))
# print("q =", repr(q))

##############################################################################
# Ejemplo

# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f"{{x:{self.x}, y:{self.y}}}"

# print("*" * 40)
# print("Definiendo solo __str__:")
# p = Punto(3,5)
# q = Punto(1,8)
# print("print")
# print("p =", p)
# print("q =", q)
# print("str")
# print("p =", str(p))
# print("q =", str(q))
# print("repr")
# print("p =", repr(p))
# print("q =", repr(q))

##############################################################################
# Ejemplo

# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.x}, {self.y})"

# print("*" * 40)
# print("Definiendo solo __repr__:")
# p = Punto(3,5)
# q = Punto(1,8)
# print("print")
# print("p =", p)
# print("q =", q)
# print("str")
# print("p =", str(p))
# print("q =", str(q))
# print("repr")
# print("p =", repr(p))
# print("q =", repr(q))

##############################################################################
# Ejemplo

# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f"{{x:{self.x}, y:{self.y}}}"
    
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.x}, {self.y})"


# print("*" * 40)
# print("Definiendo __str__ y __repr__:")
# p = Punto(3,5)
# q = Punto(1,8)
# print("print")
# print("p =", p)
# print("q =", q)
# print("str")
# print("p =", str(p))
# print("q =", str(q))
# print("repr")
# print("p =", repr(p))
# print("q =", repr(q))

##############################################################################
# Ejemplo

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{{x:{self.x}, y:{self.y}}}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    
    def __call__(self, mensaje):
        print(mensaje, self)
    
print("*" * 40)
print("Definiendo __call__:")
p = Punto(3,5)
q = Punto(1,8)
p("Hola, soy p:")
q("Hola, soy q:")

##############################################################################
