Conversor binario
========================

Como ejemplo para las siguientes declaraciones, usaremos el número entero `28`,
cuya representación binaria es `11100`:

* El bit menos significativo en una representación binaria es el bit de más a
la derecha.
* Para saber cual es el bit menos significativo de un número entero,
solo basta con calcular el sobrante módulo 2 del número en cuestión.
    * En nuestro caso, `28 % 2` es igual a `0`, lo cual concuerda con su 
    representación binaria.
* Si el bit menos significativo de una representación binaria es `0`, podemos
convertirlo en `1` sumando `1` al número correspondiente.
    * En nuestro caso, el bit menos significativo de `28` es `0,` y `28+1` 
    es `29`, cuya representación binaria es `11101`, que concuerda con cambiar a `1`
    el bit menos significativo de `28`.
* Para desplazar una posición a la izquierda todos los bits de la 
representación binaria de un número entero, solo basta con multiplicar por `2`.
    * En nuestro caso, `28 * 2` es igual a `56`, cuya representación
    binaria es `111000`, lo cual concuerda con desplazar los dígitos binarios 
    de `28` una posición hacia la izquierda.
* Para desplazar una posición a la derecha todos los bits de la 
representación binaria de un número entero, solo basta con tomar la parte 
entera de dividir entre `2`.
    * En nuestro caso, `28 // 2` es igual a `14`, cuya representación
    binaria es `1110`, lo cual concuerda con desplazar los dígitos binarios de 
    `28` una posición hacia la derecha.
    * El bit menos segnificativo se perderá.


Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada 
`ConversorBinario`:

* Dicha clase debe contener un método con firma `int_a_bin(self, numero:int)`.
    * El número debe ser de tipo entero mayor o igual a `0`.
    * Dicho método debe devolver la representación binaria del número entero dado.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si el número es negativo.
* La clase debe contener otro método con firma `bin_a_int(self, binario:str)`.
    * La representación binaria dada debe ser de tipo texto.
    * Puede contener caracteres de espacio en cualquier posición.
    * Dicho método debe devolver el equivalente en entero de la representación binaria dada.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si la representación binaria no tiene ningún dígito.
        * `ValueError`: si la representación binaria contiene valores distintos de
        `0` y `1`.


Validaciones
------------

Ejemplo 1:
```python

```

Ejemplo 2:
```python

```

Ejemplo 3:
```python

```
