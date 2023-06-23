Número de tarjeta válido
========================

Un número de tarjeta bancaria tiene 16 dígitos, cuyas posiciones van de la 1 (izquierda) hasta la 16 (derecha).

Un número de tarjeta bancaria de 16 dígitos se considera válido si el resultado
de las siguientes operaciones es tiene residuo 0 al dividir por 10:

* Los dígitos en una posición par quedan intactos.
* Cada dígito en una posición impar lo duplicamos y luego sumamos sus dígitos. 
    * Ejemplo: 8 (duplicamos)-> 16 (sumamos dígitos)-> 1 + 6 = 7
* Sumamos los 16 valores finales.
* Si el resultado da residuo 0 al dividir por 10, entonces la tarjeta es válida, de otra forma no es válida.

Para validar la solución del problema, se puede tomar como base los siguientes números de tarjeta, o los números de sus tarjetas:
```
"9422 6055 0469 3364"
"5582 2585 5104 3994"
"7265 0849 0156 4491"
"7399 6402 7845 0967"
"7009 4331 3830 6336"
```

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Tarjeta`:

* El constructor de la clase debe recibir como parámetro un número de tarjeta (str), para almacenarlo como atributo.
    * El número de tarjeta puede llevar cualquier tipo y cantidad de espacios
    en cualquier posición.
    * El número de tarjeta dado debe contener 16 dígitos numéricos.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si el número de tarjeta contiene caracteres no numéricos
        * `ValueError`: si el número de tarjeta no contiene 16 dígitos
* Dicha clase debe contener un método con firma `valida(self)`.
    * El método debe retornar `True` si el número de tarjeta registrado en el constructor es válido o `False` si no lo es.
