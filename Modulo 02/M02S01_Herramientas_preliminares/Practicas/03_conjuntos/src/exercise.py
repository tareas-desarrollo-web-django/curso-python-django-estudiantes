
##############################################################################
# Definiciones

# Conjunto de los números del 1 al 10
# Aunque tenemos elementos repetidos, solo se almacenan los elementos únicos
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 5, 7}
# Conjunto de los números del 6 al 15
B = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# Conjunto de los números del 4 al 9
C = {4, 5, 6, 7, 8, 9}
# Conjunto de textos
productos = {"RAM", "SSD", "CPU"}
# Conjunto mixto
mixto = {"1.42", "43", "342.2", 1.3434, 232}
# Un conjunto vacío
vacio = set()
# Conjunto a partir de lista
conjunto_de_lista = set([1,3,4,5,6,1,2,3])
# Conjunto a partir de tupla
conjunto_de_tupla = set(("1","3","4","5","6","1","2","3"))

##############################################################################
# Operaciones

# Podemos revisar si un elemento pertenece a un conjunto
print(f"SSD está en productos: {'SSD' in productos}")

# Podemos confirmar que C es subconjunto de A
print(f"C subconjunto de A: {C <= A}")
# Pero no alrevez
print(f"A subconjunto de C: {A <= C}")

# La intersección de A con B: {6, 7, 8, 9, 10}
print(f"A intersección con B: {A & B}")

# La unión de A con B: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(f"A unión con B: {A | B}")

# La diferencia de A con B: {1, 2, 3, 4, 5}
print(f"A - B: {A - B}")
# La diferencia de B con A: {11, 12, 13, 14, 15}
print(f"B - A: {B - A}")

# La diferencia simétrica de A con B: {1, 2, 3, 4, 5, 11, 12, 13, 14, 15}
print(f"A ^ B: {A ^ B}")

##############################################################################
# Ejemplos de uso

# Para saber si todos los elementos de una lista `X` están contenidos
# en otra lista `Y`, lo que normalmente haríamos sería algo como lo siguiente
def estan_todos(X, Y):
    for c in X:
        if c not in Y:
            return False
    
    return True

# Usando conjuntos esto se simplifica de la siguiente forma
def estan_todos_set(X, Y):
    return set(X) <= set(Y)

# Ambas funciones realizan lo mismo, como vemos a continuación
S = [2,3,5]
T = [1,2,3,4,5]
print(f"[2,3,5] están en [1,2,3,4,5]: {estan_todos(S, T)}")
print(f"[2,3,5] están en [1,2,3,4,5]: {estan_todos_set(S, T)}")
print(f"[1,2,3,4,5] están en [2,3,5]: {estan_todos(T, S)}")
print(f"[1,2,3,4,5] están en [2,3,5]: {estan_todos_set(T, S)}")

##############################################################################
r""" 
Ejercicio para la clase

Implementar una función que recibe una lista de pedidos, donde cada pedido es un
diccionario de productos que mapea el nombre de un producto a la cantidad 
solicitada del producto en el pedido, como a continuiación:
[
    {
        "RAM":10, 
        "SSD":2, 
        "CPU":6,
    },
    {
        "SSD":4,
        "BOARD":2,
    },
    {
        "CPU":7,
        "FAN":1,
        "VIDEO CARD":8,
        "SSD":9,
    }
]
La función debe devolver una lista con todos los nombres de los productos 
que aparecen en todos los pedidos, sin repeticiones.
"""

def productos_unicos(pedidos):
    ...




