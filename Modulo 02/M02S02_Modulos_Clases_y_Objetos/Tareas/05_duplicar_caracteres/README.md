Duplicar caracteres
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Texto`:

* Dicha clase debe contener un método con firma `duplicar_caracteres(self, texto:str)`.
    * Debe retornar un texto, donde cada caracter se haya duplicado, por ejemplo `"hola"` $\rightarrow$ `"hhoollaa"`.
    * Excepciones (indicar un mensaje de error):
        * `TypeError`: si `texto` no es un `str`.


Validaciones
------------

Ejemplo 1:
```python
>>> t = Texto() 

>>> t.duplicar_caracteres('Hola') 
'HHoollaa'

>>> t.duplicar_caracteres('Programación en python')
'PPrrooggrraammaacciióónn  eenn  ppyytthhoonn'

>>> t.duplicar_caracteres('Desarrollo Web')
'DDeessaarrrroolllloo  WWeebb'
```
