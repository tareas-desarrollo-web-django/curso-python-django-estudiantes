Matriz transpuesta
================================================

La transpuesta de una matriz es una matriz resultante de convertir las filas en columnas y las columnas en filas, respetanto el acomodo de estas. Es decir, la primera columna se convierte en la primera fila, etc.

Por ejemplo:

$$\begin{pmatrix}
1 & 3 \\
5 & 2
\end{pmatrix}^T=
\begin{pmatrix}
1 & 5 \\
3 & 2
\end{pmatrix}$$

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Matriz`:

* El constructor de la clase debe recibir como parámetro una matriz, para almacenarla como atributo.
    * No hay restricciones en el tamaño de la matriz.
    * La matriz debe ser dada en una tupla de tuplas, cada tupla interna es una fila de la matriz.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si la matriz no es pareja, es decir, que el tamaño de sus filas no sea igual para todas. Pueden poner el mensaje que quieran.
* La clase debe contener un método con firma `transpuesta(self)`.
    * Debe retornar la transpuesta de la matriz dada en el constructor, también como una tupla de tuplas.
    * Pista: considera la función predefinida `zip`.


Validaciones
------------

Ejemplo 1:
```python
>>> m = Matriz(((3106, 2638, 734, 3429), (3316, 3820, 1512, 2155), (4931, 2760, 4693, 4041)))
>>> m.transpuesta()
((3106, 3316, 4931), (2638, 3820, 2760), (734, 1512, 4693), (3429, 2155, 4041))
```

Ejemplo 2:
```python
>>> m = Matriz(((3074, 579, 2124, 3357), (3304, 633, 527, 1710), (3440, 3917, 4811, 3689))) 
>>> m.transpuesta()
((3074, 3304, 3440), (579, 633, 3917), (2124, 527, 4811), (3357, 1710, 3689))
```

Ejemplo 3:
```python
>>> m = Matriz(((31, 4584, 3720, 1273), (1290, 744, 4649), (625, 1456, 4265, 1729)))       
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Marcos C7\Personal\Programacion\GitHub\curso-python-django\Modulo 02\M02S02_Modulos_Clases_y_Objetos\Soluciones\04_matriz_transpuesta\src\exercise.py", line 7, in __init__
    raise ValueError("Las filas no son del mismo tamaño.")
ValueError: Las filas no son del mismo tamaño.
```
