
from copy import deepcopy

##############################################################################
# Ejemplo
# print("*" * 40)

# # Tenemos una lista de componentes y asignamos una "copia"
# x = ["ssd", "ram", "cpu", "mouse"]
# y = x

# # Mostramos los valores de ambas variables
# print(x)
# print(y, "\n")

# # Agregamos un elemento a 'x' y mostramos ambas variables
# x.append("teclado")
# print(x)
# print(y, "\n")

# # Cambiamos a mayúsculas el primer elemento de 'y' y mostramos ambas variables
# y[0] = "SSD"
# print(x)
# print(y, "\n")

# # Eliminamos el segundo elemento de 'x' y mostramos ambas variables
# del x[1]
# print(x)
# print(y, "\n")

# # En todos los casos, lo que hacíamos en una variable también aplicaba a la otra

##############################################################################
# Ejemplo
# print("*" * 40)

# # Supongamos que tenemos una lista de precios y queremos trabajar sobre una
# # copia para hacer unos cálculos, por ejemplo, descontarles el 20% y sumarlos
# precios = [20.00, 80.50, 100.00, 50.00, 72.00, 25.00]
# print(f"Precios originales: {precios}")

# copia_precios = precios

# # A cada precio en la lista copia le descontamos el 20%
# for i in range(len(copia_precios)):
#     copia_precios[i] *= 0.8

# # Mostramos la suma de los descuentos
# print(f"Suma de descuentos: {sum(copia_precios)}")

# # Vemos que aunque solo modificamos los precios de la supuesta copia,
# # también resultó afectada la lista original de precios.
# print(f"Precios originales: {precios}")
# print(f"Precios copia:      {copia_precios}")

### Como corregir esto?

# ##############################################################################
# Ejemplo: similar al ejemplo anterior, pero ahora mediante una función
# print("*" * 40)

# def sumar_descuentos(lista_precios):
#     # A cada precio en la lista copia le descontamos el 20%
#     for i in range(len(lista_precios)):
#         lista_precios[i] *= 0.8
    
#     return sum(lista_precios)

# # Lista original de precios
# precios = [20.00, 80.50, 100.00, 50.00, 72.00, 25.00]
# print(f"Precios antes del cálculo:   {precios}")

# # Calculamos la suma de descuentos y la mostramos
# total_final = sumar_descuentos(precios)
# print(f"Suma de descuentos: {total_final}")

# # Vemos que aunque solo modificamos los precios de la supuesta copia,
# # también resultó afectada la lista original de precios.
# print(f"Precios después del cálculo: {precios}")

### Como corregir esto?

# ##############################################################################
# # Ejemplo 

# print("*" * 40)

# # Función que busca mensajes de error en una lista de 'mensajes'
# # Opcionalmente recibe una lista de errores ya encontrados
# def encontrar_errores(mensajes, errores=[]):
#     for m in mensajes:
#         if m.strip().lower().startswith("error"):
#             errores.append(m)
    
#     return errores

# # Lista de operaciones realizadas
# operaciones = ["venta realizada", "error de sistema", "integracion de productos"]
# # Asumimos que no tenemos erorres por lo que no enviamos segundo argumento
# mensajes_error = encontrar_errores(operaciones)
# print(f"Erores: {mensajes_error}")

# # Nueva lista de operaciones realizadas
# operaciones = ["error de terminal", "venta realizada", "pago realizado"]
# # Como ya tenemos errores no procesados, los mandamos
# mensajes_error = encontrar_errores(operaciones, mensajes_error)
# print(f"Erores: {mensajes_error}")

# # Nueva lista de operaciones realizadas
# operaciones = ["pago realizado", "venta realizada", "pago rechazado"]
# # Asumimos que ya hemos procesado los erroes y por lo tanto no enviamos
# # segundo argumento
# mensajes_error = encontrar_errores(operaciones)
# print(f"Erores: {mensajes_error}")

### Como corregir esto?

################################################################################


# Algo mucho más básico

# Hemos visto que podemos replicar un número en una lista
numeros = [5] * 4

# Estaríamos tentados a hacer algo similar si quisiéramos inicializar una lista de listas vacías
filas = [[]] * 5
print(filas)

# El problema es que en realidad la multiplicación lo que hace es replicar la referencia, no el objeto
filas[0].append(3)
print(filas)

### Como corregir esto?

################################################################################