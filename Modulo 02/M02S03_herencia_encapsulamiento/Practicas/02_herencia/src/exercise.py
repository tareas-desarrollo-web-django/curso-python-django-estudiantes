
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
# Ejemplo

# class Perro:
#     def __init__(self, color):
#         print("Constructor: Perro")
#         self.color = color
#         self.patas = 4
#         self.ojos = 2
#         self.colmillos = 4
#         self.sonido = "Guaau"
    
#     def hablar(self):
#         print(f"Perro hablando: {self.sonido}")
    
#     def dormir(self):
#         print(f"Perro: durmiendo")
    
#     def correr(self):
#         print(f"Perro: corriendo")

# class Pollito:
#     def __init__(self, color):
#         print("Constructor: Pollito")
#         self.color = color
#         self.patas = 2
#         self.ojos = 2
#         self.alas = 2
#         self.sonido = "pio pio"
    
#     def hablar(self):
#         print(f"Pollito hablando: {self.sonido}")
    
#     def dormir(self):
#         print(f"Pollito: durmiendo")
    
#     def volar(self):
#         print(f"Pollito: volando")


# class PerroPollito(Perro, Pollito):
#     def __init__(self, color):
#         Pollito.__init__(self, color)
#         Perro.__init__(self, color)

#     def dormir(self):
#         print("PerroPollito: durmiendo más chido")

#     def lanzar_rayo_laser(self):
#         print("PerroPollito: lanzando laser")


# perro_pollito = PerroPollito("cafe")

# print("*" * 40)
# perro_pollito.hablar()
# perro_pollito.dormir()
# perro_pollito.correr()
# perro_pollito.volar()
# print(vars(perro_pollito))


##############################################################################


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
#         super().__init__(color, 4, 2)
#         print("Constructor: Perro")
#         self.colmillos = 4
#         self.sonido = "Guaau"
        
    
#     def hablar(self):
#         super().dormir()
#         print(f"Perro hablando: {self.sonido}")

# class Ave(Animal):
#     def __init__(self, color):
#         super().__init__(color, 2, 2)
#         print("Constructor: Ave")
#         self.alas = 2
    
#     def caminar(self):
#         print("Ave: caminando")

# class Pollito(Ave):
#     def __init__(self, color):
#         super().__init__(color)
#         print("Constructor: Pollito")
#         self.sonido = "pio pio"
    
#     def hablar(self):
#         print(f"Pollito hablando: {self.sonido}")

#     def dormir(self):
#          print("Pollito: durmiendo")

# print("*" * 40)
# animal = Animal("cafe", 4, 2)
# print("*" * 40)
# perro = Perro("blanco")
# print("*" * 40)
# ave = Ave("naranja")
# print("*" * 40)
# pollito = Pollito("amarillo")

# print("*" * 40)
# animal.caminar()
# perro.caminar()
# ave.caminar()
# pollito.caminar()

# print("*" * 40)
# animal.dormir()
# perro.dormir()
# ave.dormir()
# pollito.dormir()

# print("*" * 40)
# perro.hablar()
# pollito.hablar()

##############################################################################
# Ejemplo

# class PerroPollito(Perro, Pollito):
#     def __init__(self, color):
#         # Ejecutamos el super desde Perro, porque de otra
#         # forma Perro intentará invocar el __init__ de la siguiente
#         # clase en el MRO, la cual es Pollito que recibe 1 paráemtro, 
#         # pero Perro asume que es Animal que recibe 3 parámetros.

#         # Para evitar estos problemas, lo ideal sería que la herencia tuviera
#         # los mismos niveles por ambos lados, es decir, una clase Canino entre
#         # Animal y Perro. Porque lo actual hace que perro no aporte ningún
#         # atributo.
#         super(Perro, self).__init__(color)

#     def lanzar_rayo_laser(self):
#         print("PerroPollito: lanzando laser")

# perro_pollito = PerroPollito("cafe")

# print("*" * 40)
# perro_pollito.hablar()
# perro_pollito.dormir()
# perro_pollito.caminar()
# perro_pollito.lanzar_rayo_laser()
# print(vars(perro_pollito))

##############################################################################
# Ejemplo

# class A:
#     def __inits__(self):
#         print("A")
#         self.val = "a"

# class B:
#     def __inits__(self):
#         print("B")
#         self.val = "b"

# class X(A, B):
#     def __inits__(self):
#         print("X")
#         self.val = "x"

# class Y(A, B):
#     def __inits__(self):
#         print("Y")
#         self.val = "y"

# class Z(X, Y):
#     def __init__(self):
#         super().__init__()
#         print("Z")

##############################################################################
