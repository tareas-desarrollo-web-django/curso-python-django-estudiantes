Filtrar objetos instanciados desde una clase
================================================

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Computadora`:

* El constructor de la case debe recibir como parámetros los siguientes, para almacenarlos como atributos:
    * Un texto que representa el tipo de computadora y solo puede tomar uno de los valores `"pc"`, `"laptop"`, o `"tableta"`.
    * Un ID entero y único.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si el tipo de computadora no es una opción válida.
        * `ValueError`: si el ID ya está siendo usado por otra computadora.
* Dicha clase debe contener un método con firma `filtrar(self, tipo_computadora:str)`.
    * El parámetro `tipo_computadora` debe ser uno de `"pc"`, `"laptop"`, o `"tableta"`.
    * Dicho método debe retornar un conjunto con todos los IDs de los objetos que han sido creados y que tengan el tipo especificado.
    * Excepciones (indicar un mensaje de error):
        * `ValueError`: si `tipo_computadora` no es una opción válida.

