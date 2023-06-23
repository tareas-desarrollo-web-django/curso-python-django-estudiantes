import math

class Entero:
    def __init__(self, numero):
        if not isinstance(numero, int):
            raise ValueError("El número no es entero")
        if numero <= 0:
            raise ValueError("El número no debe ser <= 0")

        self.numero = numero
            
    def factorizar(self):
        n = self.numero
        
        factores = []
        k = 2
        while k <= math.sqrt(n):
            if n % k == 0: 
                # Si 'k' divide a 'n', entonces lo agregamos como factor primo
                # y dividimos el número por 'k', pero nos quedamos en el mismo
                # valor de 'k'.
                factores.append(k)
                n //= k
            else:
                # Si 'k' no divide a 'n', entonces ya podemos avanzar al siguiente
                k += 1
        
        # Agregamos el último valor de 'n', ya que es un número primo al no 
        # tener divisores 'k <= math.sqrt(n)'.
        factores.append(n)
        
        return factores


if __name__ == "__main__":
    n = Entero(89)
    print(n.factorizar())