r"""
Ejemplos de prácticas
"""

##############################################################################

def procesar_datos(lat, lng, edo, mun, loc):
    # Asumimos que aquí se hace un procesamiento
    print("\nProcesando datos")
    print(f"{lat=}, {lng=}, {edo=}, {mun=}, {loc=}")

# Nombres de columnas
columnas = ["Precios unitarios", "Cantidades en existencia"]
# Separamos los nombres de columnas en identificadores más claros
col_precios, col_existencias = columnas
print(f"{col_precios = }")
print(f"{col_existencias = }")

# Datos geográficos
datos_geo = [19.239805, -103.709148, "06", "002", "0001"]
# Separamos la latitud y la longitud del resto de valores
lat, lng, *claves = datos_geo
print(f"{lat=}")
print(f"{lng=}")
print(f"{claves=}")

# Invocamos la función desempaquetando manualmente
procesar_datos(datos_geo[0], datos_geo[1], datos_geo[2], datos_geo[3], datos_geo[4])
# Invocamos la función desempaquetando automáticamente
procesar_datos(*datos_geo)

##############################################################################
# Desempaquetado de valores cuando una función retorna una tupla o lista

def residuo(a, b):
    r"""Devuelve el entero y el residuo de dividir 'a' con 'b'"""
    entero = a // b
    residuo = a % b
    return (entero, residuo)

entero, residuo = residuo(23, 7)
print(f"{entero=}, {residuo=}")

##############################################################################
# Desempaquetado al iterar sobre iterables

# Mediante un iterable directo
precios_productos = [('Libreta', 30.90), ('Lirbo', 43.30), ('Plumones',80.40), ('Carpetas', 323.10)]
for producto, precio in precios_productos:
    print(f"{producto=}, {precio=}")

# Mediante un genrador de iterables, como el caso del método 'items' de un 
# diccionario
precios_productos = {'Libreta':30.90, 'Lirbo':43.30, 'Plumones':80.40, 'Carpetas':323.10}
for producto, precio in precios_productos.items():
    print(f"{producto=}, {precio=}")

##############################################################################

