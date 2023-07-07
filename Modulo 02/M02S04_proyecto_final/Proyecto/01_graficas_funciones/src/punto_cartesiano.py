import math

class PuntoCartesiano:
    r"""
    Clase que implementa la funcionalidad de un Punto en el plano Cartesiano.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        r"""Representación descriptiva del punto en forma (x, y)"""
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        r"""Representación constructiva del punto"""
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def magnitud(self):
        r"""Distancia del origen al punto"""
        return math.sqrt((self.x * self.x) + (self.y * self.y))
    
    def __neg__(self):
        r"""Devuelve un punto nuevo cambiando los signos de las coordenadas """
        return self.__class__(-self.x, -self.y)
    
    def __add__(self, otro):
        r"""Devuelve un punto nuevo igual a la suma del mismo punto con `otro`"""
        if isinstance(otro, self.__class__):
            return self.__class__(self.x + otro.x, self.y + otro.y)
        elif isinstance(otro, list|tuple):
            return self.__class__(self.x + otro[0], self.y + otro[1])
    
    def __sub__(self, otro):
        r"""Devuelve un punto nuevo igual a la resta del mismo punto con `otro`"""
        if isinstance(otro, list|tuple):
            otro = self.__class__(*otro)
        return self + (-otro)
    
    def __mul__(self, otro):
        r"""Devuelve un punto nuevo igual a la multiplicación coordenada
        a coordenada del mismo punto con `otro`.
        Donde `otro` puede ser una tupla, una lista, una instancia de
        esta clase o un escalar.
        """
        if isinstance(otro, self.__class__):
            return self.__class__(self.x * otro.x, self.y * otro.y)
        elif isinstance(otro, list|tuple):
            return self.__class__(self.x * otro[0], self.y * otro[1])
        elif isinstance(otro, int|float):
            return self.__class__(self.x * otro, self.y * otro)
    
    def tupla(self):
        r"""Devuelve las coordenadas del punto pero en forma de una tupla"""
        return (self.x, self.y)