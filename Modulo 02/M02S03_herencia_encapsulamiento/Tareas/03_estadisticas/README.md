Estadísticas
========================

El promedio $\mu$ de una lista de números $a_1, ..., a_n$ es:
$$\mu = \frac{a_1 + ... + a_n}{n}$$

La varianza es:
$$\sigma^2 = \frac{(a_1 - \mu)^2 + ... + (a_n - \mu)^2}{n}$$

Problema
--------

Crea un módulo llamado `src\estadisticas.py` que contenga una clase llamada `Estadisticas`:

* El constructor de la clase debe recibir como parámetro una lista de números, para almacenarla como atributo.
    * Los números pueden ser `int` o `float`.
    * La lista puede ser vacía.
* La clase debe contener un método con firma `promedio(self)`.
    * Debe regresar el promedio de los números dados en el constructor.
    * El resultado debe estar redondeado a 6 dígitos decimales.
* La clase debe contener un método con firma `varianza(self)`.
    * Debe regresar la varianza de los números dados en el constructor.
    * El resultado debe estar redondeado a 3 dígitos decimales.
