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
