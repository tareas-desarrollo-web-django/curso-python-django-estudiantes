from copy import deepcopy

# Un módulo puede contener cualquier código.

class Matriz2x2:
    def __init__(self, M):
        if len(M) != 2 or set(map(len, M)) != {2}:
            raise ValueError("La matriz no es de 2x2")

        self.matriz = deepcopy(M)
        self.filas = len(M)
        self.columnas = len(M[0])
    
    def sumar(self, M2):
        if isinstance(M2, self.__class__):
            M2 = M2.matriz
        
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] += M2[i][j]
    
    def print(self, prefijo):
        fila_str = lambda f: "\t".join(map(str, f))
        print(prefijo)
        print("\n".join(map(fila_str, self.matriz)))


def mensaje_diagonal(mensaje):
    for i,c in enumerate(mensaje):
        print(" " * i + c)