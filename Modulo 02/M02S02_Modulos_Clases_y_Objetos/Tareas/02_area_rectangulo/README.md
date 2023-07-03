Area de un rectángulo
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Rectangulo`:

* El constructor de la clase debe recibir como parámetros la base (float) y la altura (float) de un rectángulo, en ese orden, para almacenarlos como atributos.
* La clase debe contener un método con firma `area(self)`.
    * No recibe parámetros.
    * Debe retornar el áera del rectángulo al que representa la instancia, redondeado a 2 decimales.


Validaciones
------------

Ejemplo 1:
```python
>>> from exercise import Rectangulo
>>> r = Rectangulo(48.5, 8.0)
>>> r.area()
388.0
```

Ejemplo 2:
```python
>>> r = Rectangulo(42.2, 40.0)
>>> r.area()
1688.0
```

Ejemplo 3:
```python
>>> r = Rectangulo(25.4, 3.7)  
>>> r.area()
93.98
```