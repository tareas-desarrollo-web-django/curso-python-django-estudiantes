Métodos mágicos (dunder) de uso general
=============================================

La forma en la que Python incorpora sobrecarga de operadores es a través de métodos especiales llamados ***dunder*** o ***mágicos***. Dunder viene de combinar las palabas **d**ouble-**under**score, ya que los métodos mágicos inician y terminan don doble guión bajo.

Sintaxis:
----------

Aquí veremos los métodos mágicos de uso general:
* `__repr__`: lo ideal es que este método regrese un texto que se vea como una expresión válida de Python que se pueda usar para recrear el objeto. Si no es posible, entonces debe regresar información útil del objeto de la forma `<... informacion del objeto ...>`.
* `__str__`: este método debe regresar un texto que describa de manera amigable el objeto y su contenido. Es lo que se muestra al invocar `print()` o la función `str()` sobre el objeto. Si este no está definido, entonces se usará `__repr__` en su lugar.
* `__call__`: si se implementa este método en una clase, entonces todas sus instancias podrán ser invocables como si fueran funciones, y esta es la función que se ejecutará cuando el objeto se invoque.