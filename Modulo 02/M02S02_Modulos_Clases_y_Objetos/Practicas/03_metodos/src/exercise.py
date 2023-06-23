'''
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
'''

##############################################################################
# Definiciones

class Auto:
    def __init__(self, nombre:str, color:str, vel_max_kmh:int):
        self.nombre = nombre
        self.color = color
        self.vel_max_kmh = vel_max_kmh
        self.vel_actual = 0
    
    def arrancar(self, vel:int):
        if vel > self.vel_max_kmh:
            raise ValueError(f"No se puede superar la velocidad máxima de {self.vel_max_kmh} km/h")
        
        print(f"Arrancando el auto a {vel} km/h")
        self.vel_actual = vel
    
    def frenar(self):
        print(f"Frenando el auto")
        self.vel_actual = 0
    
    def sumar_numeros(self, a, b):
        return a + b

##############################################################################
# Operaciones

# # Creamos un Auto llamado Taxi.
taxi = Auto("Taxi", "Amarillo", 150)

# taxi.frenar(10, 20)

# # Invocamos sus métodos
# print(f"Velocidad inicial: {taxi.vel_actual}")
# taxi.arrancar(100)
# print(f"Velocidad actual: {taxi.vel_actual}")
# taxi.frenar()
# print(f"Velocidad al frenar: {taxi.vel_actual}\n")

# # Intentemos superar la velocidad máxima
# try:
#     taxi.arrancar(200)
# except ValueError as e:
#     print(e)

##############################################################################