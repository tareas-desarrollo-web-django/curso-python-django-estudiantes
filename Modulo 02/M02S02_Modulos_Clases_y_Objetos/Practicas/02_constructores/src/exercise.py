'''
Constructores de clase
'''

##############################################################################
# Definiciones

class Auto:
    def __init__(self, nom, llan=4, col="Rojo", vel=200):
        self.nombre = nom
        self.llantas = llan
        self.color = col
        self.vel_max_kmh = vel

        print(f"Se ha construido un auto con nombre {self.nombre}\n")

# Generamos dos instancias de la clase Auto
# El único parámetro obligatorio es el nombre
taxi = Auto("Taxi", 4, "Rojo", 150)
deportivo = Auto("Deportivo", 4, "Rojo", 400)

##############################################################################
# Operaciones

# Mostramos los atributos
print("Atributos iniciales")
print(f"{taxi.nombre}:")
print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
print(f"{deportivo.nombre}:")
print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}\n")

# Cambiamos algunos valores de los atributos
deportivo.vel_max_kmh = 400
deportivo.color = "Naranja"

# Volvemos a mostrar los atributos
print("Atributos modificados")
print(f"{taxi.nombre}:")
print(f"{taxi.color=}, {taxi.llantas=}, {taxi.vel_max_kmh=}")
print(f"{deportivo.nombre}:")
print(f"{deportivo.color=}, {deportivo.llantas=}, {deportivo.vel_max_kmh=}\n")

##############################################################################