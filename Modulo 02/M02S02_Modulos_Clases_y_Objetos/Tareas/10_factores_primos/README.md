Factorización prima
================================================

Un número primo $p$ es un entero que no es divisible de manera exacta por ningún número $ 2 \leq d \leq p-1$.

La factorización prima de un número entero $N\geq 1$, es la descomposición del número como una multiplicación de puros números primos. Por ejemplo:

$$45423 = 3\cdot 3 \cdot 7 \cdot 7 \cdot 103$$

Los números $3,3,7,7,103$ son los factores primos del número $45423$.

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Entero`:

* El constructor de la clase debe recibir como parámetro un número entero para almacenarlo en un atributo.
    * El número debe ser estrictamente mayor que cero.
    * Excepciones del constructor (indicar cualquier mensaje de error):
        * `ValueError`: si el número dado no es entero
        * `ValueError`: si el número dado no es mayor que cero
* Dicha clase debe contener un método con firma `factorizar(self)`.
    * Debe retornar una lista de los factores primos del número especificado en el constructor.
    * La lista debe estar ordenada del más pequeño al más grande.

Tips para resolver el problema:
* Un número divide a otro si el residuo de la división es cero.
* El factor primo más pequeño de un número $N$ es igual al entero más chico ($\geq 2$) que divide al número, es decir, ni siquiera tenemos que revisar si el divisor es primo.


Validaciones
------------

Ejemplo 1:
```python
>>> n = Entero(909483172)
>>> n.factorizar()
[2, 2, 13, 191, 91571]
```

Ejemplo 2:
```python
>>> n = Entero(947089220) 
>>> n.factorizar()        
[2, 2, 5, 7, 11, 67, 67, 137]
```

Ejemplo 3 (excepción en el constructor):
```python
>>> n = Entero(-483)      
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Marcos C7\Personal\Programacion\GitHub\curso-python-django\Modulo 02\M02S02_Modulos_Clases_y_Objetos\Soluciones\10_factores_primos\src\exercise.py", line 8, in __init__
    raise ValueError("n no debe ser <= 0")
ValueError: n no debe ser <= 0
```
