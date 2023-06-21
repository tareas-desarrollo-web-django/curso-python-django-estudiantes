
##############################################################################
# Definiciones

def dividir_numeros(a, b):
    if b == 0:
        raise ZeroDivisionError("b es cero")
    
    return a / b

def sumar_numeros(a, b):
    if not isinstance(a, float|int):
        raise TypeError("a no es numérico")
    if not isinstance(b, float|int):
        raise TypeError("b no es numérico")
    
    return a + b


def fibonacci(n):
    if n < 0:
        raise ValueError("n es negativo")
    
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

