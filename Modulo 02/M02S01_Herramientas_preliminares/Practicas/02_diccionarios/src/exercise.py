r"""
Ejemplos de prácticas
"""

##############################################################################

# Un diccionario de precios
# precios_productos = {'Libreta':30.90, 'Libro':43.30, 'Plumones':80.40, 'Carpetas':323.10}

# Podemos obtener un iterable con las puras llaves y otro con los puros valores
# llaves = precios_productos.keys()
# valores = precios_productos.values()

# Al iterar sobre un diccionario directamente, en realidad se está iterando 
# sobre las llaves:
# for x in precios_productos:
#     print(x)

# Si queremos iterar sobre las parejas, tenemos que usar el método 'items', 
# lo cual itera en tuplas (llave, valor), donde la llave es el primer elemento
# y el valor es el segundo.
# for x in precios_productos.items():
#     print(f"Objeto: {x}")
#     print(f"Llave: {x[0]}, valor: {x[1]}")
#     print('-' * 10)

# Revisamos si un producto está definido en el diccionario de precios
# libro_definido = 'Libro' in precios_productos
# lapiz_definido = 'Lápiz' in precios_productos
# print(f"Libro tiene precio?: {libro_definido}")
# print(f"Lápiz tiene precio?: {lapiz_definido}")

##############################################################################

# Diccionario anidado (estilo JSON)
# respuesta = {
#     'estado': 'OK',
#     'mensaje': 'Operación exitosa',
#     'pedidos':[
#         {
#             'id_pedido': 10,
#             'id_usuario': 12,
#             'total': 117.50,
#             'productos':[
#                 {
#                     'id': 2,
#                     'nombre': 'Libreta',
#                     'precio': 30.90,
#                     'cantidad': 1
#                 },
#                 {
#                     'id': 5,
#                     'nombre': 'Libro',
#                     'precio': 43.30,
#                     'cantidad': 2
#                 }
#             ]
#         },
#         {
#             'id_pedido': 12,
#             'id_usuario': 71,
#             'total': 303.00,
#             'productos':[
#                 {
#                     'id': 7,
#                     'nombre': 'Plumones',
#                     'precio': 80.40,
#                     'cantidad': 3
#                 },
#                 {
#                     'id': 2,
#                     'nombre': 'Libreta',
#                     'precio': 30.90,
#                     'cantidad': 2
#                 }
#             ]
#         }
#     ]
# }

# Consultamos el estado y el mensaje de la respuesta
# print(f"Estado: {respuesta['estado']}")
# print(f"Mensaje: {respuesta['mensaje']}")

# Mostramos en consola el contenido del primer pedido y también de sus productos
# pedido = respuesta['pedidos'][0]
# productos = pedido['productos']
# print(f"Pedido: {pedido}")
# print(f"Productos: {productos}")

# def calcular_total_pedidos(respuesta):
#     r"""
#     Recibe una respuesta con pedidos y calcula el costo total de todos los pedidos
#     """
#     total = 0.0
#     for pedido in respuesta['pedidos']:
#         total += pedido['total']
#     return total

# Mostramos el costo total de todos los pedidos
# total_pedidos = calcular_total_pedidos(respuesta)
# print(f"Total de todos los pedidos: {total_pedidos}")

##############################################################################
r""" 
Ejercicio para la clase

Usando el mismo objeto 'respuesta' definido anteriormente, implementa una 
función que:
- Reciba: dicho objeto 'respuesta'.
- Devuelva: un diccionario que contenga los usuarios que realizaron pedidos
  y cuantos pedidos realizó cada usuario. Las llaves del diccionario deben 
  ser los IDs de los usuarios y los valores deben ser el número de pedidos.
  Solo debe contener los usuarios que aparecen en los pedidos.
"""

def pedidos_usuarios(respuesta):
    ...

##############################################################################
r""" 
Ejercicio para la clase

Usando el mismo objeto 'respuesta' definido anteriormente, implementa una 
función que:
- Reciba: dicho objeto 'respuesta'.
- Devuelva: un diccionario que contenga cuanto se pidió de cada producto 
  tomando en cuenta todos los pedidos. Las llaves del diccionario deben 
  ser los nombres de los productos y los valores deben ser las cantidades.
  Solo debe contener los productos que aparecen en los pedidos.
"""

def productos_pedidos(respuesta):
    ...

##############################################################################
