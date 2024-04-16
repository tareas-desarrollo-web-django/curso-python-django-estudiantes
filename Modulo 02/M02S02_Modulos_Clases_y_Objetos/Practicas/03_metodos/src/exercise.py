
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
r"""
Ejercicio para realizar en clase
- Generar una clase llamada 'Tabla' que menje una tabla desde un csv
- La clase debe recibir en el constructor un paráemtro `ruta` con la ruta del 
  archivo csv y automáticamente cargar la tabla, la tabla se espera que tenga 
  una cabecera y el contenido de valores enteros.
- Debe tener un método `guardar(ruta:str)` para guardar el contenido de la 
  tabla de vuelta al archivo.
- Implementar un método `sumar(k:int)` para sumarle una constante a toda la 
  tabla.
"""


##############################################################################