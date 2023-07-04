'''
Métodos mágicos (dunder) para emular álgebra
===================================================

Aquí continuamos con los métodos mágicos (o dunder), pero ahora veremos algunos que se suelen usar para que un objeto soporte operaciones algebráicas personalizadas.

Sintaxis:
----------

* `__neg__`: dar soporte para cambiar el signo al objeto en cuestión, con el operador unario `-`.
* `__add__`: agregar soporte para sumar un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `+`.
* `__sub__`: agregar soporte para restar un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `-`.
* `__mul__`: agregar soporte para multiplicar un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `*`.
* `__truediv__`: agregar soporte para dividir un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `/`.
* `__floordiv__`: agregar soporte para dividir a piso un objeto del mismo o de diferente tipo, al objeto en cuestión, con el operador `//`.
* `__ld__`: agregar soporte para comparar si el objeto en cuestión es menor que un objeto del mismo o de diferente tipo, con el operador `<`.
* `__le__`: agregar soporte para comparar si el objeto en cuestión es menor o igual que un objeto del mismo o de diferente tipo, con el operador `<=`.
* `__gt__`: agregar soporte para comparar si el objeto en cuestión es mayor que un objeto del mismo o de diferente tipo, con el operador `>`.
* `__ge__`: agregar soporte para comparar si el objeto en cuestión es mayor o igual que un objeto del mismo o de diferente tipo, con el operador `>=`.
* `__eq__`: agregar soporte para comparar si el objeto en cuestión es igual que un objeto del mismo o de diferente tipo, con el operador `==`.
* `__ne__`: agregar soporte para comparar si el objeto en cuestión es diferente que un objeto del mismo o de diferente tipo, con el operador `!=`.
'''

##############################################################################
# Ejemplo
import math

class PuntoCartesiano:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def magnitud(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))
    
    def __neg__(self):
        return self.__class__(-self.x, -self.y)
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x + other.x, self.y + other.y)
        elif isinstance(other, list|tuple):
            return self.__class__(self.x + other[0], self.y + other[1])
    
    def __sub__(self, other):
        if isinstance(other, list|tuple):
            other = self.__class__(*other)
        return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x * other.x, self.y * other.y)
        elif isinstance(other, list|tuple):
            return self.__class__(self.x * other[0], self.y * other[1])
    
    def __le__(self, other):
        if isinstance(other, list|tuple):
            other = self.__class__(*other)
        return self.magnitud() <= other.magnitud()
    
    def __eq__(self, other):
        if isinstance(other, list|tuple):
            other = self.__class__(*other)
        return (self.x == other.x) and (self.y == other.y)
#

p = PuntoCartesiano(1,5)
q = PuntoCartesiano(3,6)
r = PuntoCartesiano(1,5)

# # Reflejamos un punto
# print(f"-{p} = {-p}")
# # Sumamos puntos
# print(f"{p} + {q} = {p+q}")
# # Restamos puntos
# print(f"{p} - {q} = {p-q}")
# # Multiplicamos puntos
# print(f"{p} * {q} = {p*q}")
# # Comparamos puntos
# print(f"|{p}|={p.magnitud():.2f} <= |{q}|={q.magnitud():.2f}? {p<=q}")
# print(f"{p} == {q}? {p==q}")
# print(f"{p} == {r}? {p==r}")

##############################################################################
