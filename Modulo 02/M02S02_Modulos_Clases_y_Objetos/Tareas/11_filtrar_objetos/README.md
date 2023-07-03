Filtrar objetos instanciados desde una clase
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Computadora`:

* El constructor de la case debe recibir como parámetros los siguientes, para almacenarlos como atributos:
    * Un texto que representa el tipo de computadora y solo puede tomar uno de los valores válidos que son: `"pc"`, `"laptop"`, o `"tableta"`.
    * Un ID entero y único.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si el tipo de computadora no es una opción válida.
        * `ValueError`: si el ID ya está siendo usado por otra computadora.
* Dicha clase debe contener un método con firma `filtrar(self, tipo_computadora:str)`.
    * El parámetro `tipo_computadora` debe ser uno de `"pc"`, `"laptop"`, o `"tableta"`.
    * El objetivo del método es poder consultar desde cualquier objeto `Computadora` un filtrado de los objetos que son del tipo de computadora especificado.
    * Debe retornar un `conjunto` con todos los IDs de los objetos que han sido creados y que tengan el tipo especificado.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si `tipo_computadora` no es una opción válida.

Tips para resolver el problema:
* Usar atributos de clase para llevar un registro de los objetos que han sido creados.

Validaciones
------------

Ejemplo 1:
```python
# Tipos de computadoras y IDs
>>> elementos = [('tableta', 512930772), ('tableta', 892638676), ('pc', 140800980), ('tableta', 807303636), ('tableta', 57820116), ('pc', 27172308), ('laptop', 120312788), ('laptop', 525968852), ('pc', 119057876), ('laptop', 
365219284), ('tableta', 519238612), ('laptop', 296200148), ('pc', 357738964), ('laptop', 850005460), ('tableta', 894345684), ('laptop', 145509332), ('pc', 37137364), ('tableta', 846701012), ('pc', 750525396), ('laptop', 638813652), ('tableta', 973159892), ('laptop', 423305684), ('tableta', 640646100), ('laptop', 839684564), ('laptop', 614527444), ('laptop', 893556180), ('laptop', 501371860), ('tableta', 332459476), ('laptop', 207874516), ('tableta', 785206740), ('laptop', 316195796)]

# Los objetos en una lista
>>> computadoras = [Computadora(nombre, id) for nombre, id in elementos]

# Excepción al intentar usar un ID que ya fue usado, aunque tenga distinto tipo
>>> repetido = Computadora('pc', 512930772)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Marcos C7\Personal\Programacion\GitHub\curso-python-django\Modulo 02\M02S02_Modulos_Clases_y_Objetos\Soluciones\11_filtrar_objetos\src\exercise.py", line 14, in __init__
    raise ValueError(f"ID {compu_id} no disponible")
ValueError: ID 512930772 no disponible

# Obtenemos los IDs de los objetos que son de tipo 'tableta'
>>> computadoras[0].filtrar('tableta') 
{785206740, 57820116, 892638676, 512930772, 807303636, 519238612, 894345684, 846701012, 973159892, 640646100, 332459476}

# Obtenemos los IDs de los objetos que son de tipo 'pc'
>>> computadoras[0].filtrar('pc')      
{119057876, 357738964, 27172308, 140800980, 37137364, 750525396}

# Obtenemos los IDs de los objetos que son de tipo 'laptop'
>>> computadoras[0].filtrar('laptop') 
{501371860, 316195796, 207874516, 893556180, 365219284, 525968852, 120312788, 296200148, 850005460, 145509332, 638813652, 423305684, 839684564, 614527444}

# Excepción por un tipo no válido
>>> computadoras[0].filtrar('telefono') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Marcos C7\Personal\Programacion\GitHub\curso-python-django\Modulo 02\M02S02_Modulos_Clases_y_Objetos\Soluciones\11_filtrar_objetos\src\exercise.py", line 23, in filtrar
    raise ValueError("Tipo de computadora no válido")
ValueError: Tipo de computadora no válido
```

