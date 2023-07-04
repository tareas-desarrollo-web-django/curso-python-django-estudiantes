'''
Módulos
=========

En Python, un módulo es simplemente un script `.py`:
* El nombre del archivo será el nombre del módulo, por ejemplo si el script se llama `mi_modulo.py`, entonces el nombre del módulo será `mi_modulo`.
* Todos lo que esté dentro del módulo formará parte de los componentes del módulo.
* Para importar un módulo solo hacemos uso de `import`: por ejemplo, `import mi_modulo`.
    * Todos los componentes del módulo (funciones, clases, variables, etc) serán accesibles a través del espacio de nombres `mi_modulo`, por ejemplo: `mi_modulo.mi_funcion()`.
* Podemos importar componentes en particular de un módulo con `from`.
    * Por ejemplo: `from mi_modulo import mi_funcion`
    * De esa forma ya podemos usar `mi_funcion` directamente sin usar como prefijo el módulo.
'''

##############################################################################
# Ejemplo: Módulo con rutas de arvivos

# import rutas

# print("*" * 40)
# print(rutas.archivo_ventas)
# print(rutas.archivo_catalogo)
# print(rutas.archivo_pedidos)
# print(rutas.archivo_inventario)

# from rutas import archivo_pedidos

# print("*" * 40)
# print(archivo_pedidos)


##############################################################################
# Ejemplo: módulo de matriz

# from matriz_2x2 import Matriz2x2

# print("*" * 40)
# M1 = Matriz2x2([[1,2], [3,4]])
# M2 = Matriz2x2([[5,6], [7,8]])
# print("Matrices iniciales")
# M1.print("M1:")
# M2.print("M2:")
# M1.sumar(M2)
# print("M2 sumada a M1")
# M1.print("M1:")
# M2.print("M2:")
# print("Identidad sumada a M1")
# M1.sumar([[1,0], [0,1]])
# M1.print("M1:")

# from matriz_2x2 import mensaje_diagonal
# mensaje_diagonal("Matrices")

##############################################################################

