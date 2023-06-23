Fibonacci con caché
========================

La serie Fibonacci es una sucesión de números cuyos primeros dos elementos
son `0` y `1`. Cualquier elemento siguiente se calcula como la suma de sus
dos elementos anteriores.

Esta sucesión se expresa matemáticamente como sigue, donde `f(n)` representa
el `n-ésimo` elemento de la sucesión, con `n >= 0`:

* `f(0) = 0`
* `f(1) = 1`
* `f(n) = f(n - 1) + f(n - 2)`

IMPORTANTE: para poder ejecutar `pytest` en este problema, es necesario instalar `pytest-timeout`:
* `pip install pytest-timeout`

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Fibonacci`:

* Dicha clase debe contener un método con firma `elemento(self, n:int)`.
    * El parámetro `n` es un entero `>= 0`.
    * Dicho método debe retornar el `n-ésimo` elemento de la sucesión 
    de Fibonacci.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si `n` es menor que cero.
* La implementación se debe hacer con recursividad.
* En esta ocación la clase debe manejar un pequeño sistema de caché mediante atributos, donde se registren los elementos de Fibonacci que ya han sido calculados.
    * De esta forma, podemos revisar en el caché si ya fue calculado el 
    `i-ésimo` elemento y usarlo en lugar de volver a calcularlo.
