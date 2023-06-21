
##############################################################################
# Definiciones
import os
from datetime import datetime

# Expresión que convierte una fecha "dd/mm/aaaa" en objeto datetime
dt = lambda f: datetime.strptime(f, "%d/%m/%Y")
# Expresión que convierte un datetime a texto con formato "dd/mm/aaaa"
dt_str = lambda f_dt: f_dt.strftime("%d/%m/%Y")
# Expresión que calcula el número de días para llegar de una fecha a otra
diferencia_dias = lambda f1, f2: (dt(f2) - dt(f1)).days
# Expresión que eleva un número al cuadrado
cuadrado = lambda n: n * n
# Expresión que recibe un texto que contiene enteros separados por coma, 
# lo convierte a una lista de enteros
texto_a_lista = lambda texto: list(map(int, texto.split(",")))
# Expresión que convierte una lista de elementos a un texto separado por coma
lista_a_texto = lambda lista: ",".join(map(str, lista))

##############################################################################
# Operaciones

# Datetime con la fecha de navidad
navidad = dt("25/12/2022")
# Datetime con la fecha de independencia
independencia = dt("16/09/2022")
# Mostramos la fecha de intependencia a la consola en formato "dd/mm/aaaa"
print(f"Dia de independencia: {dt_str(independencia)}")

# Lista de los primeros 10 números cuadrados
cuadrados = [cuadrado(i) for i in range(1, 11)]
print(f"Primeros 10 cuadrados: {cuadrados}")

##############################################################################
# Ejemplos de uso

# Cargamos una matriz de números (sin cabecera) desde un csv
def cargar_matriz(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        return list(map(texto_a_lista, archivo.readlines()))

# Guardamos una matriz en un csv
def guardar_matriz(matriz, ruta_archivo):
    with open(ruta_archivo, "w") as archivo:
        archivo.write("\n".join(map(lista_a_texto, matriz)))

# Ruta de la carpeta que contiene el csv con la matriz
ruta_carpeta = os.path.dirname(__file__)
# Llamamos la carga de la matriz
matriz = cargar_matriz(ruta_carpeta + "\\matriz.csv")
# Guardamos la misma matriz pero en un archivo diferente
guardar_matriz(matriz, ruta_carpeta + "\\matriz_2.csv")

##########################

# Hay funciones que para generalizar su aplicación, esperan como parámetro
# una o más funciones.

# Funciones de ordenamiento predefinidas en Python
coordenadas = [(2, 6), (9, 10), (2, 3), (4, 9), (8, 7), (8, 4), (10, 1), (2, 7)]
# Podemos ordenadar las coordenadas. Por defecto, las tuplas se ordenadn primero respecto
# al primer elemento, luego respecto al segundo, etc. 
sorted(coordenadas)
# Podemos ordenarlas en orden inverso usando el argumento 'reverse'
# pero esta limitado a solo invertir el orden de la lista
sorted(coordenadas, reverse=True)
# Otra forma de ordenar en orden inverso es usar el argumento 'key', que es más
# general y nos permite tener control total respecto al orden de los elementos.
# Este argumento espera una función, y es aquí donde podemos hacer uso de las
# expresiones 'lambda', si no requerimos de algo muy sofisticado.
sorted(coordenadas, key=lambda x: (-x[0], -x[1]))
# Podemos or ejemplo en su lugar ordenar de mayor a menor por la primera entrada pero 
# de menor a mayor por la segunda coordenada.
sorted(coordenadas, key=lambda x: (-x[0], x[1]))
# O podemos ordenar como prioridad por la segunda coordenada
sorted(coordenadas, key=lambda x: (x[1], x[0]))
# O podemos solamente ordenar tomando en cuenta la primera coordenada
sorted(coordenadas, key=lambda x: x[0])




