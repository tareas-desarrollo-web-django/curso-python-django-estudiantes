Solucionador de sistema de ecuaciones lineales
================================================

El determinante de una matriz de 2x2 se calcula como sigue:

$$\begin{vmatrix}
a & b \\
c & d 
\end{vmatrix} =
a\cdot d - c\cdot b$$

Un sistema de 2 ecuaciones lineales con 2 incógnitas es de la forma:

$$
\begin{matrix}
a\cdot x + b\cdot y = e \\
c\cdot x + d\cdot y = f \\
\end{matrix}$$

De acuerdo a la regla de Cramer, la solución a dicho sistema de ecuaciones se puede resolver con determinantes mediante la siguiente fórmula:

$$
\begin{matrix}
x = \frac{\begin{vmatrix}
e & b \\
f & d 
\end{vmatrix}}
{\begin{vmatrix}
a & b \\
c & d 
\end{vmatrix}}
& \qquad
y = \frac{\begin{vmatrix}
a & e \\
c & f 
\end{vmatrix}}
{\begin{vmatrix}
a & b \\
c & d 
\end{vmatrix}}
\end{matrix}
$$

Nótese que el sistema solo tiene solución si 
$$\begin{vmatrix}
a & b \\
c & d 
\end{vmatrix} \neq 0$$

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Ecuaciones`:

* El constructor de la clase debe recibir como parámetros los coeficientes de un sistema de ecuaciones como el descrito arriba, para almacenarlos como atributos.
    * El primer parámetro debe recibir los coeficientes de la primera ecuación en forma de tupla: `(a, b, e)`.
    * El segundo parámetro debe recibir los coeficientes de la segunda ecuación en forma de tupla: `(c, d, f)`.
    * Excepciones del constructor (indicar cualquier mensaje de error):
        * `ValueError`: si alguna de las tuplas de coeficientes no contiene 3 elementos.
        * `ValueError`: si alguna de las tuplas de coeficientes contiene valores no numéricos (`int|float`).
* La clase debe contener un método con firma `determinante(self, M:tuple)`.
    * `M` es una matriz de 2x2 en forma de tuplas, ej. `((2, 5),(1, 8.1))`
    * Debe devolver el determinante de dicha matriz.
    * Excepciones (indicar cualquier mensaje de error):
        * `ValueError`: si `M` no es de 2x2.
* También debe contener un método con firma `resolver(self)`.
    * No recibe parámetros porque las ecuaciones a resolver son las especificadas en el constructor.
    * Dicho método debe retornar un diccionario donde la llave `"x"` mapea a la solución $x$ del sistema, y la llave `"y"` mapea a la solución $y$ del sistema.
    * Ambos valores deben ser redondeados a 5 dígitos decimales.
    * Si el sistema no tiene solución ambas llaves del diccionario deben ser `None`.


Validaciones
------------

Ejemplo 1:
```python
>>> e = Ecuaciones((-882, -164, 458), (-169, -652, 759)) 
>>> e.determinante(((112, 357), (-937, 420)))            
381549
>>> e.resolver()                                         
{'x': -0.31815, 'y': -1.08164}
```

Ejemplo 2:
```python
>>> e = Ecuaciones((18, -90, -223), (156, -780, 608))
>>> e.determinante(((27, -133), (-950, -736)))
-146222
>>> e.resolver()
{'x': None, 'y': None}
```

Ejemplo 3 (excepción en el constructor):
```python
>>> e = Ecuaciones((8, 156), (546, 46, 232))          
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Marcos C7\Personal\Programacion\GitHub\curso-python-django\Modulo 02\M02S02_Modulos_Clases_y_Objetos\Soluciones\09_ecuaciones_lineales\src\exercise.py", line 7, in __init__
    raise ValueError("Coeficientes de eucación 1 no válidos")
ValueError: Coeficientes de eucación 1 no válidos
```
