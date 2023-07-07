
##############################################################################
# Ejemplo

# class Triangulo:
#     def dibujar(self, contexto):
#         print(f"Dibujando triángulo en {contexto}")

# class Rectangulo:
#     def dibujar(self, contexto):
#         print(f"Dibujando rectángulo en {contexto}")

# class Poligono:
#     def dibujar(self, contexto):
#         print(f"Dibujando polígono en {contexto}")

# class CurvaBezier:
#     def dibujar(self, contexto):
#         print(f"Dibujando curva de bezier en {contexto}")

# class GraficaFuncion:
#     def dibujar(self, contexto):
#         print(f"Dibujando gráfica de función en {contexto}")


# def dibujar_escena(figuras, contexto):
#     for figura in figuras:
#         figura.dibujar(contexto)

# # Lista de figuras
# figuras = [Triangulo(), Rectangulo(), Poligono(), Triangulo(),
#     CurvaBezier(), GraficaFuncion(), Rectangulo(), GraficaFuncion()]

# # Dibujamos todas las figuras de la lista
# print("*" * 40)
# dibujar_escena(figuras, "ventana_1")

# figuras.append(Rectangulo())
# print("*" * 40)
# dibujar_escena(figuras, "ventana_1")

##############################################################################
# Ejemplo

# from random import randint

# class PagoPaypal:
#     def procesar_pago(self, monto):
#         print(f"Pagando con Paypal: {monto}")

# class PagoTarjeta:
#     def procesar_pago(self, monto):
#         print(f"Pagando con Tarjeta: {monto}")

# class PagoTransferencia:
#     def procesar_pago(self, monto):
#         print(f"Pagando con Transferencia: {monto}")

# class PagoEfectivo:
#     def procesar_pago(self, monto):
#         print(f"Pagando con Efectivo: {monto}")


# class Carrito:
#     def calcular_total(self):
#         return randint(1000, 10000) / 100

#     def pagar(self, metodo):
#         monto = self.calcular_total()
#         metodo.procesar_pago(monto)

# print("*" * 40)
# carrito = Carrito()
# carrito.pagar(PagoPaypal())
# carrito.pagar(PagoTarjeta())
# carrito.pagar(PagoTransferencia())
# carrito.pagar(PagoEfectivo())

##############################################################################
