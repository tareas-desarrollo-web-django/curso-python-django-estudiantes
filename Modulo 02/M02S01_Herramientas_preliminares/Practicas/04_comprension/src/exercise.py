
##############################################################################
# Definiciones

import math


# Conjunto de números pares menores a 40
pares_40 = {i for i in range(40) if i % 2 == 0}
# Conjunto de números impares menores a 1000
impares_1000 = {i for i in range(1000) if i % 2 == 1}
# Conjunto de los números que son cuadrados perfectos menores a 1000
cuadrados_1000 = {i * i for i in range(1, math.ceil(math.sqrt(1000)))}
# Conjunto de números menores a 1000 que al dividirlos por 5 sobra 1
cinco_residio_1 = set(range(1, 1000, 5))
# Lista de tuplas (i, j) donde `0 <= i <= 4` y `0 <= j <= 3`
tuplas_cartesianas = [(i, j) for i in range(5) for j in range(4)]

##############################################################################
# Operaciones

# Números pares menores a 40 que no son cuadrados perfectos
pares_no_cuadrados = pares_40 - cuadrados_1000
print(f"Pares menores a 40 que no son cuadrados: {pares_no_cuadrados}")

# Conjunto de los cuadrados perfectos menores que 1000, 
# que además son impares, y al dividirlos por 5 sobra 1.
conjunto_raro = cuadrados_1000 & impares_1000 & cinco_residio_1
print(f"Cuadrados, impares y residuo 1 % 5: {conjunto_raro}")
# Lo mismo pero en una lista ordenados de menor a mayor
print(f"Cuadrados, impares y residuo 1 % 5 (ordenados): {sorted(conjunto_raro)}")

# Lista de tuplas (i, j) donde `0 <= i <= 4` y `0 <= j <= 3` y `i + j == 6`
tuplas_cartesianas_suma_6 = [p for p in tuplas_cartesianas if p[0] + p[1] == 3]
print(f"Tuplas (0<=i<=4, 0<=j<=3) con i+j=6: {tuplas_cartesianas_suma_6}")

##############################################################################

# Añadir prefijos o sufijos
columnas = ['promedio', 'varianza', 'desviacion', 'confianza_a', 'confianza_b']
columnas_alumnos = [f"{c}_alumnos" for c in columns]
columnas_maestros = [f"{c}_maestros" for c in columns]

##############################################################################
r""" 
Ejercicio para la clase

El módulo `os` sirve para realizar operaciones en el sistema operativo.
Algunas de sus funciones son las siguientes:
- `os.listdir(directorio)`: retorna la lista de archivos y carpetas en un directorio.
- `os.path.isfile(ruta)`: retorna True si la ruta corresponde a un archivo y retorna
  False si corresponde a un directorio.

Elaborar una función que reciba un directorio y retorne una lista con todos
los archivos que contiene, excluyendo los directorios. También recibe un 
parámetro opcional `extension` que si el invocador manda una extensión, 
entonces la función solo debe retornar los archivos que contengan dicha
extensión (como 'pdf', 'csv', etc).
"""

import os
def obtener_archivos(directorio, extension=None):
    ...


