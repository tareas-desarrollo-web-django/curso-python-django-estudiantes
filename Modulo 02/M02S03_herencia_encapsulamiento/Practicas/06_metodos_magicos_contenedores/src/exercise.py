'''
Métodos mágicos (dunder) para simular contenedores
===================================================

Aquí continuamos con los métodos mágicos (o dunder), pero ahora veremos algunos que se suelen usar para que un objeto se comporte como si fuera un contenedor.

Sintaxis:
----------

* `__len__`: debe devolver el número de elementos que simula tener el contendor, se invoca automáticamente al usar la función `len()` sobre un objeto.
* `__getitem__`: debe devolver una referencia al elemento asociado a la llave (o índice). Se invoca automáticamente al consultar con el operador `[]`.
    * Ejemplo: `mi_objeto[5]`, o `mi_objeto["a"]`, etc.
* `__setitem__`: debe asignar un nuevo valor al elemento asociado a la llave (o índice). Se invoca automáticamente al asignar valores con el operador `[]`.
    * Ejemplo: `mi_objeto[5] = 10`, o `mi_objeto["a"] = 20`, etc.
* `__delitem__`: debe eliminar al elemento asociado a la llave (o índice). Se invoca automáticamente al borrar con el operador `[]`.
    * Ejemplo: `del mi_objeto[5]`, o `del mi_objeto["a"]`, etc.
* `__contains__`: debe retornar `True` si el existe un elemento asociado a la llave (o índice) indicado. Se invoca automáticamente con `in`.
    * Ejemplo: `5 in mi_objeto`, o `"a" in mi_objeto`, etc.
'''

##############################################################################
# Ejemplo

from pathlib import Path

class ManejadorDatos:
    def __init__(self):
        self.cache_datos = {}
        self.carpeta_datos = Path(__file__).parent / "datos"
    
    def __len__(self):
        return len(self.cache_datos)
    
    def __getitem__(self, key):
        if key not in self.cache_datos:
            print(f"--Cargando archivo {key}--")
            with (self.carpeta_datos / key).open() as f:
                self.cache_datos[key] = f.read()
        
        return self.cache_datos[key]
    
    def __setitem__(self, key, val):
        self.cache_datos[key] = val
    
    def __delitem__(self, key):
        if key in self.cache_datos:
            del self.cache_datos[key]
    
    def __contains__(self, key):
        return key in self.cache_datos
#

datos = ManejadorDatos()

# Vemos como se muestra el contenido de archivos, los cuales
# se cargan automáticamente, gracias a la implementación
# del método __getitem__.
print("*" * 40)
print(datos["ventas.csv"])
print(datos["ventas.csv"])
print("*" * 40)
print(datos["catalogo.csv"])
print(datos["catalogo.csv"])
print("*" * 40)
print(datos["inventario.csv"])
print(datos["inventario.csv"])

# Vemos que la implementación del método __setitem__ solo remplaza
# el contenido, pero como sigue existiendo la llave, ya no se vuelve 
# a cargar al consultarlo.
print("*" * 40)
datos["inventario.csv"] = "ya no soy el archivo inventario"
print(datos["inventario.csv"])

# Pero si borramos la llave con el método __delitem__, entonces se vuelve
# a cargar al consultarlo.
print("*" * 40)
del datos["inventario.csv"]
print(datos["inventario.csv"])

# Prodemos consultar pertenencia gracias al método __contains__
print("*" * 40)
print(f"Archivo 'ventas.csv' cargado? {'ventas.csv' in datos}")
print(f"Archivo 'pedidos.csv' cargado? {'pedidos.csv' in datos}")
        

##############################################################################
