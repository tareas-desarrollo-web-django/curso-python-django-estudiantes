from typing import Union

class Ecuaciones:
    def __init__(self, eq1, eq2):
        if (len(eq1) != 3 or 
            not all([isinstance(v, Union[int,float]) for v in eq1])):
            raise ValueError("Coeficientes de eucación 1 no válidos")
        if (len(eq2) != 3 or 
            not all([isinstance(v, Union[int,float]) for v in eq2])):
            raise ValueError("Coeficientes de eucación 1 no válidos")
        
        self.eq1 = eq1
        self.eq2 = eq2
    
    def determinante(self, M):
        if len(M) != 2 or len(M[0]) != 2 or len(M[1]) != 2:
            raise ValueError("La matriz no es de 2x2")
        return M[0][0] * M[1][1] - M[1][0] * M[0][1]
    
    def resolver(self):
        M = ((self.eq1[0], self.eq1[1]), (self.eq2[0], self.eq2[1]))
        Mx = ((self.eq1[2], self.eq1[1]), (self.eq2[2], self.eq2[1]))
        My = ((self.eq1[0], self.eq1[2]), (self.eq2[0], self.eq2[2]))

        det_M = self.determinante(M)
        if det_M != 0:
            x = self.determinante(Mx) / det_M
            y = self.determinante(My) / det_M
            return {"x":round(x, 5), "y":round(y, 5)}
        else:
            return {"x":None, "y":None}

if __name__ == "__main__":
    sistema = Ecuaciones((311, 175, -701), (-842, 511, -54))
    # sistema = Ecuaciones((8, -18*5, -223), (156, -156*5, 608))