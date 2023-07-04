Derivada de funciones
========================

La derivada de una función $f(x)$ se puede aproximar mediante la siguiente fórmula:

$$f'(x) = \frac{f(x+h) - f(x-h)}{2\cdot h}$$

El valor de $h$ indica que tan precisa es la aproximación, mientras más cercano a cero sea, más precisa la derivada.

Problema
--------

Crea un módulo llamado `src\funcion.py` el cual contenga una clase llamada `Funcion`:

* El constructor de la clase debe recibir como parámetro una función en forma de expresión lambda, para almacenarla como atributo.
    * La expresión lambda debe recibir un número float y regresar un número float, por ejemplo: `lambda x: x**2`
* La clase debe contener un método con firma `derivada(self, x:float, h:float)`.
    * El método debe devolver la derivada en `x` de la función dada en el constructor, en la precisión indicada por `h`.
    * El resultado debe estar redondeado a 3 dígitos decimales.
