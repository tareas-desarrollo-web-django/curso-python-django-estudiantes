r"""
Ejemplos de prácticas
"""

##############################################################################
# Desempaquetado básico

# Nombres de columnas
columnas = ["Precios unitarios", "Cantidades en existencia"]
# Separamos los nombres de columnas en identificadores más claros
col_precios, col_existencias = columnas

# Podemos desempaquetar estructuras anidadas replicando la estructura con las variables
nombre, (x, y) = ['A', (1, 5)]

# Generalmente en Python, cuando un valor no va a ser usado, generalmente en ciclos, se usa el nombre '_'
ancho, alto, _ = (23, 5, 'cuadrado')

########################################
# Desempaquetado con '*'

# A izquierda
*coord, edo, mun, loc = [19.239805, -103.709148, "06", "002", "0001"]
# A la derecha
lat, lng, *claves = [19.239805, -103.709148, "06", "002", "0001"]
# Enmedio
lat, lng, *_, loc = [19.239805, -103.709148, "06", "002", "0001"]

########################################
# Desempaquetado en parámetros posicionales

def procesar_datos(lat, lng, edo, mun, loc):
    # Asumimos que aquí se hace un procesamiento
    print("\nProcesando datos")
    print(f"{lat=}, {lng=}, {edo=}, {mun=}, {loc=}")

datos_geo = [19.239805, -103.709148, "06", "002", "0001"]
# Podemos invocar la función desempaquetando manualmente
procesar_datos(datos_geo[0], datos_geo[1], datos_geo[2], datos_geo[3], datos_geo[4])
# Pero es mejor usar el desempaquetado
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

########################################
# Mediante un genrador de iterables, como el caso del método 'items' de un diccionario

# Precios de productos
precios_productos = {'Libreta':30.90, 'Lirbo':43.30, 'Plumones':80.40, 'Carpetas':323.10}
for producto, precio in precios_productos.items():
    print(f"{producto=}, {precio=}")

########################################
# Con anidación

# Diccionario de foreignkeys
foreignkeys = {'fk_up':('usuario', 'pedido'), 'fk_pd':('pedido', 'direccion'), 'fk_ep':('estado', 'pedido')}
for fk, (origen, destino) in foreignkeys.items():
    print(f"Hay un foreignkey llamado {fk}, del origen {origen} al destino {destino}")

##############################################################################
# Desempaquetado de parámetros  con diccionarios

def consultar_bd(conexion, tabla, columnas, filtros=None):
    print('Consultando la base de datos..')
    print(f"{conexion=}")
    print(f"{tabla=}")
    print(f"{columnas=}")
    print(f"{filtros=}")

    return [['id', 'nombre'], [2, 'Libreta'], [3, 'Libro']]


# Podemos intercambiar el orden, ya que al ir con nombre la relación es única
consulta = {
    'conexion': 'sqlalchemy',
    'tabla': 'productos',
    'columnas': ['id', 'nombre'],
    'filtros': ["nombre in ('Libreta', 'Libro')"]
}

# Desempaquetando de parámetros manual
datos = consultar_bd(consulta['conexion'], consulta['tabla'], consulta['columnas'], consulta['filtros'])
# Desempaquetando de parámetros automático
datos = consultar_bd(**consulta)

##############################################################################