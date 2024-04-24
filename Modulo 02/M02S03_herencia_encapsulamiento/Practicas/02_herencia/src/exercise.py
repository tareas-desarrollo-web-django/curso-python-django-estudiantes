
##############################################################################
# # Ejemplo
# # El constructor es solo un método, su única particularidad es que
# # se ejecuta automáticamente al crear una instancia, pero puede
# # ejecutarse manualmente como si fuera cualquier otro método.

# class Animal:
#     def __init__(self, color, patas, ojos):
#         print("Constructor: Animal")
#         self.color = color
#         self.patas = patas
#         self.ojos = ojos
    
#     def caminar(self):
#         print("Animal: caminando")
    
#     def dormir(self):
#         print("Animal: durmiendo")


# # Creamos un perro de tipo Animal
# perro = Animal("cafe", 4, 2)
# # Mostramos los atributos de la variable 'perro'
# print("Perro:")
# print(vars(perro), "\n")

# # El constructor como es un método cualquiera, podemos invocarlo también.
# perro.__init__("blanco", 3, 5)
# # Mostramos nuevamente los atributos de la variable 'perro'
# print("Perro:")
# print(vars(perro), "\n")

##############################################################################
# Ejemplo

# class Animal:
#     def __init__(self, color, patas, ojos):
#         print("Constructor: Animal")
#         self.color = color
#         self.patas = patas
#         self.ojos = ojos
    
#     def caminar(self):
#         print("Animal: caminando")
    
#     def dormir(self):
#         print("Animal: durmiendo")

# class Perro(Animal):
#     def __init__(self, color):
#         super().__init__(color, patas=4, ojos=2)
#         print("Constructor: Perro")
#         self.ojos = 8
#         self.colmillos = 4
#         self.sonido = "Guaau"

#     def hablar(self):
#         print(f"Perro hablando: {self.sonido}")


# labrador = Perro("cafe", 4, 2)
# labrador.caminar()
# labrador.dormir()
# labrador.hablar()
# print(vars(labrador))


##############################################################################
# Composición sobre herencia

# class Domicilio:
#     def __init__(self, calle, numero, colonia):
#         self.calle = calle
#         self.numero = numero
#         self.colonia = colonia
    
#     def calcular_coordenadas(self):
#         print("Calculando coordenadas en base al domicilio")

# class Salarios:
#     def __init__(self, nombre_empleado):
#         self.nombre_empleado = nombre_empleado
#         self.sueldo_base = None
#         self.aguinaldo = None
#         self.cargar_datos()
    
#     def cargar_datos(self):
#         print(f"Cargando salarios de {self.nombre_empleado} de la base de datos")

# class Empleado:
#     def __init__(self, nombre_empleado):
#         self.domicilio = Domicilio("Benito Juarez", 324, "Bellavista")
#         self.salarios = Salarios(nombre_empleado)
#         self.edad = 24
#         self.estudios = "ingenirería"
#         self.sexo = "hombre"
    
#     def programar_recoleccion(self):
#         coordenadas = self.domicilio.calcular_coordenadas()
#         print("Empleado listado en la ruta")

