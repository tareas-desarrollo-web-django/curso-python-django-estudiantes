Indicadores de tipo en funciones
==================================

Python permite una sintaxis auxiliar para indicar el tipo de dato esperado para un parámetro en una función, así como el tipo de dato retornado por la función:
* Es una sintaxis meramente auxiliar para el programador.
* Así el programador puede ver que tipos de datos se esperan para los parámetros de una función, sin tener que revisar el código o la documentación.
* El intérprete ignora completamente los indicadores de tipo, por lo que la función se puede invocar con cualquier tipo de dato distinto al indicado

Sintaxis:
----------

* Para indicar el tipo de dato esperado para un parámetro, la sintaxis es: `parametro:tipo_esperado`
    * Ejemplo, elevar 5 a una pótencia dada: `elevar_5(potencia:int):`
* Además del tipo esperado también podemos establecer un valor por defecto con la sintaxis: `parametro:tipo_esperado=valor_defecto`
    * Ejemplo, la potencia por defecto será 2: `elevar_5(potencia:int=2):`
* Cada parámetro puede llevar su indicador: 
    * `elevar(base:float, potencia:int):`
* Se puede indicar también el tipo de dato que retornará la función con `->`:
    * `elevar(base:float, potencia:int) -> float:`
    * `procesar(datos:list) -> None:`
* Se puede indicar varios tipos de dato esperados o retornados, separándolos con la barra `|`:
    * Ejemplo: `elevar(base:float|int, potencia:int) -> float|int:`
    * La barra solo funciona desde Python 3.10 en adelante.
    * Anteriormente se hacía con: `Union[float, int]`