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
    * El parámetro `meses` debe ser entero e indica que se quiere pronosticar la deuda existente ese número de meses a partir de ahora.
    * Debe devolver la deuda pronosticada al último mes.
    * Los intereses se suman a la deuda cada mes en base a la tasa de interes mensual.
    * El resultado se debe devolver redondeado a 2 dígitos decimales.
    * El resultado no puede ser negativo, si la deuda se paga en ese periodo, debe retornar 0.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si `meses` es menor que cero.

