Pronóstico de deuda
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Deuda`:

* El constructor de la clase debe recibir como parámetros la deuda actual (float), el interés mensual (float) y el pago mensual (float), en ese orden, para almacenarlos como atributos.
    * Todos esos valores deben ser $\geq 0$.
    * El interés debe ser un número que representa un porcentaje, por ejemplo, `10` significa el 10%.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si algún valor es menor que cero.
* Dicha clase debe contener un método con firma `pronosticar_deuda(self, meses:int)`.
    * El parámetro `meses` debe ser entero.
    * Debe devolver el pronóstico de cuanto se deberá al mes dado como parámetro.
    * Los intereses se suman a la deuda cada mes, después de haber aplicado el pago mensual.
    * El resultado se debe devolver redondeado a 2 dígitos decimales.
    * El resultado no puede ser negativo, si la deuda se paga en ese periodo, debe retornar 0.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si `meses` es menor que cero.
* Ejemplo:
    * Si la deuda actual es `d_ini = 9829914.3`, el interés mensual es `r = 2` %, y el pago mensual es de `p = 481858.54`.
    * La deduda al final de los próximos 3 `meses` será:
        * Al mes `0`: $d_0 = d_{ini} = 9829914.3$
        * Al mes `1`: $d_1 = (d_0 - 481858.54) * 1.02 = 9535016.8752$
        * Al mes `2`: $d_2 = (d_1 - 481858.54) * 1.02 = 9234221.5019$
        * Al mes `3`: $d_2 = (d_2 - 481858.54) * 1.02 = 8927410.2211$
        * Por lo que la deuda después de 3 meses, redondeada a 2 decimales será: `8927410.22`


Validaciones
------------

Ejemplo 1:
```python
>>> d = Deuda(9829914.3, 2, 481858.54)
>>> d.pronosticar_deuda(3) 
8927410.22
```

Ejemplo 2:
```python
>>> d = Deuda(4663451.86, 15, 648828.08) 
>>> d.pronosticar_deuda(15) 
2444562.57
```

Ejemplo 3 (excepción en el constructor):
```python
>>> d = Deuda(46351.86, 4, -8828.08)     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Marcos C7\Personal\Programacion\GitHub\curso-python-django\Modulo 02\M02S02_Modulos_Clases_y_Objetos\Soluciones\06_deuda\src\exercise.py", line 6, in __init__
    raise ValueError("No se permiten valores negativos")
ValueError: No se permiten valores negativos
```

Ejemplo 4 (exepción en el método):
```python
>>> d = Deuda(46351.86, 4, 8828.08)  
>>> d.pronosticar_deuda(-2) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Marcos C7\Personal\Programacion\GitHub\curso-python-django\Modulo 02\M02S02_Modulos_Clases_y_Objetos\Soluciones\06_deuda\src\exercise.py", line 14, in pronosticar_deuda
    raise ValueError("los meses no deben ser menos que cero")
ValueError: los meses no deben ser menos que cero
```
