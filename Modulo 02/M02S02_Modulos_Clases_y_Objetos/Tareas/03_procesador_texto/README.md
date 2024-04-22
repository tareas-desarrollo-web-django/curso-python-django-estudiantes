Procesador de texto
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `ProcesadorTexto`:

* Dicha clase debe contener un método con firma `remover_espacios(self, texto:str)`.
    * El parámetro `texto` debe ser cualquier texto, con cualquier cantidad y tipo de caracteres de espacio, ya sean espacios normales, tabuladores, saltos de linea, etc.
    * Debe retornar el texto, pero con todos los espacios removidos de todos los lugares.
    * Pista: considera la función `split` de `str`.


Validaciones
------------

Ejemplo 1:
```python
>>> p = ProcesadorTexto()

>>> p.remover_espacios('fLKUX\th\nHuUbp\tf\t\nL\nh\t gsCi\nq \nwImQis\t\nJKy\trqhbxn hEq\t IVS\nUS') 
'fLKUXhHuUbpfLhgsCiqwImQisJKyrqhbxnhEqIVSUS'

>>> p.remover_espacios('\nb \t O\n\t HtrkiPSE \t \tUU iW\tq D X\n\noMcsG t\tXravEisvINF  Fl\tU\n ')  
'bOHtrkiPSEUUiWqDXoMcsGtXravEisvINFFlU'

>>> p.remover_espacios('\tJg wUq\nMkpX \tg dOjvt\tWau\tvv\nnL\tw \tgj iWvIDWSR ykMikyDd OJVr\t\nt\tW Hj\nY\n') 
'JgwUqMkpXgdOjvtWauvvnLwgjiWvIDWSRykMikyDdOJVrtWHjY'
```
