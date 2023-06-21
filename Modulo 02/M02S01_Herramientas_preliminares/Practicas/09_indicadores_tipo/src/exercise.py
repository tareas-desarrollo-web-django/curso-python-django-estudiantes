
##############################################################################
# Definiciones
import os

ruta_carpeta = os.path.dirname(__file__)

# Indicamos un tipo de dato esperado en el parámetro
def duplicar_texto(texto:str):
    return texto * 2

# Indicamos dos tipos de dato esperados para cada parámetro y para el retorno
def sumar_numeros(a:int|float, b:int|float) -> int|float:
    return a + b

# Solo especificamos tipos esperados para un parámetro
def multiplicar_numeros(a:int|float, b) -> int|float:
    return a * b

# None también puede ser un tipo esperado y podemos asignar un valor 
# por defecto al parámetro, en este caso el valor por defecto es None
def cargar_texto(ruta_archivo:str|None=None) -> str:
    if ruta_archivo is None:
        ruta_archivo = ruta_carpeta + "\\archivo_default.txt"
    
    with open(ruta_archivo, "r") as archivo:
        return archivo.read()


def elevar(a:int, n:int=2):
    return a ** n

def sumar(a, b=2, c=3, d=4, e=5):
    return a + b + c + d + e
