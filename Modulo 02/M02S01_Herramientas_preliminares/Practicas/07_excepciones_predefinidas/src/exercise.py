
##############################################################################
# Definiciones

def dividir_numeros(a, b):
    r"""Divide el número 'a' con el 'b'"""
    if b == 0:
        raise ZeroDivisionError("b es cero")
    
    return a / b

def sumar_numeros(a, b):
    r"""Suma los números 'a' y 'b'"""
    if not isinstance(a, float|int):
        raise TypeError("'a' tiene que ser numérico")
    if not isinstance(b, float|int):
        raise TypeError("'b' tiene que ser numérico")
    
    return a + b


def fibonacci(n):
    r"""Calcula y retorna el n-ésimo número de la serie Fibonacci"""
    if n < 0:
        raise ValueError("'n' no puede ser negativo")
    
    if n <= 1:
        return n
    
    return fibonacci(n - 2) + fibonacci(n - 1)


##############################################################################
# - Ciclo de sumas sin manejar excepciones. El programa terminará con error
# al proveer texto en lugar de número.
# - Le agregaremos un poco de manejo de excepciones, para que el programa no
# termine cuando ocurra un error al convertir a enteros los valores dados
# por el usuario.

salir = False
while not salir:
    print('Opciones')
    print('1.- Sumar dos números')
    print('2.- Salir')
    opc = input('Ingresa el número de la opción: ').strip()
    
    if opc == '1':
        x = input('Ingresa los números separados por espacio: ').split()
        print(f">>> La suma es {int(x[0]) + int(x[1])}")
    elif opc == '2':
        salir = True
    else:
        print("No es una opción válida")
    
    print(""'*' * 40)