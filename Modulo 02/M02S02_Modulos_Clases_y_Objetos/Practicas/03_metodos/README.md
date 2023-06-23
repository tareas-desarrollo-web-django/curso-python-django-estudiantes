Métodos
=========

Los ***Métodos*** son funciones ligadas a una clase que determinan el comportamiento y las interacciones que tendrán los objetos instanciados con el resto del código.

Lo idea es cada clase tenga un propósito específico para que sus métodos estén relacionados. Por ejemplo, no sería intuitivo crear una clase que tenga revueltos los atributos de un limón y de un gato. Lo mejor sería tener una clase para un limón y otra clase para un gato.

Sintaxis:
----------

* Los métodos deben estar definidos dentro de la clase a la que corresponden.
* La sintaxis es similar que el de una función normal, solo que su primer argumento `self` siempre recibirá el objeto sobre el que se está aplicando el método.
    * Ejemplo: `def mover(self, pasos):`.
* El nombre del primer argumento no tiene que ser `self` necesariamente, pero utilizar otro nombre implicaría mucha confusión, ya que el primer argumento siempre será el objeto sobre el que se aplica el método y es enviado automáticamente por Python al invocar el método.
    * Por favor nunca usen otro nombre distinto a `self` para el primer argumento de un método.