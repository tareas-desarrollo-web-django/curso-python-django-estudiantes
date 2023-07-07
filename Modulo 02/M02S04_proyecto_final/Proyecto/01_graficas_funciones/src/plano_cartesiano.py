import pdb
import sys
import pygame
import math
import time
from random import randint
from copy import deepcopy
# from exercise import PuntoCartesiano
from punto_cartesiano import PuntoCartesiano


# Colores etiquedatos
class Color:
    r"""
    Conjunto de colores predefinidos accesibles a tráves de esta clase.
    """
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)
    BLANCO = (255, 255, 255)
    GRIS_CLARO = (240, 240, 240)
    GRIS = (200, 200, 200)


class PlanoCartesiano:
    r"""
    Clase que simula un plano cartesiano, con funciones básicas para dibujar 
    lineas, circulos y puntos en el plano.
    """
    def __init__(self, color_fondo:tuple|Color, ancho:int, alto:int, x_dominio:tuple, y_dominio:tuple):
        r"""
        Constructor de la clase.

        Args:
            color_fondo (tuple|COlor): color de fondo para usar en el plano, 
                es dado en una tupla (r,g,b), con valores entre 0 y 255.
            ancho (int): ancho en pixeles de la ventana sobre la que se 
                dibujará el plano.
            alto (int): alto en pixeles de la ventana sobre la que se 
                dibujará el plano.
            x_dominio (tuple): rango visible del eje 'x' del plano cartesiano.
            y_dominio (tuple): rango visible del eje 'y' del plano cartesiano.
        """
        # Inicializamos los elementos de 'pygame'
        pygame.init()

        # Color de fondo
        self.color_fondo = color_fondo
        # Ancho y alto en pixeles del área de dibujado
        self.ancho = ancho
        self.alto = alto
        # Para dibujar elementos en la ventana como si estuvieramos en un
        # plano cartesiano, el área de dibujado es mapeada a un cominio
        # cartesiano:
        #   x_dominio=(x_0,x_1) define el intervalo para el dominio de x
        #   y_dominio=(y_0,y_1) define el intervalo para el dominio de y
        self.x_dominio = None
        self.y_dominio = None

        # Configuración de elementos predefinidos
        self.ejes = True
        self.marcas_sep = 1
        self.cuadricula = True

        # Ajustamos el dominio de manera segura
        self.ajustar_dominio(x_dominio, y_dominio)

        # Ventana donde dibujaremos
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))

        # Atributos para click y arrastrar
        self.arrastrando = False
        self.mouse_pos = None
        self.alt = False
        self.ctrl = False

        # Contador de tiempo
        self.tiempo = time.time()
    
    def ajustar_dominio(self, x_dominio, y_dominio):
        r"""
        Cambiamos el dominio visible del plano cartesiano. El dominio puede
        quedar un poco estirado si no hay una relación precisa entre el dominio
        de 'x' y el dominio de 'y'.

        Args:
            x_dominio (tuple): rango visible del eje 'x' del plano cartesiano.
            y_dominio (tuple): rango visible del eje 'y' del plano cartesiano.
        """
        if x_dominio is None or y_dominio is None:
            raise ValueError("Los dominios no pueden ser 'None'")
        
        self.x_dominio = deepcopy(x_dominio)
        self.y_dominio = deepcopy(y_dominio)
        # Make sure that x_0 < x_1 and y_0 < y_1
        if self.x_dominio[1] < self.x_dominio[0]:
            self.x_dominio = (self.x_dominio[1], self.x_dominio[0])
        if self.y_dominio[1] < self.y_dominio[0]:
            self.y_dominio = (self.y_dominio[1], self.y_dominio[0])
    
    def ajustar_dominio_proporcional(self, x_dominio=None, y_dominio=None, encuadre=None):
        r"""
        Cambiamos el dominio visible del plano cartesiano. En este caso nos
        aseguramos de que el dominio visible no quete estirado.

        El encuadre, horizontal o vertical, es para especificar si queremos que
        el dominio 'x' quede perfectamente ajustado a la ventana (encuadre 
        horizontal), o si queremos que el dominio 'y' sea el que quede 
        perfectamente ajustado a la ventana (encuadre vertical).
        Notemos que solo un encuadre va a contener completamente al dominio
        especificado.

        Args:
            x_dominio (tuple): rango visible del eje 'x' del plano cartesiano.
                Si es None, entonces se usará `self.x_dominio`.
            y_dominio (tuple): rango visible del eje 'y' del plano cartesiano.
                Si es None, entonces se usará `self.y_dominio`.
            encuadre (str): "h" para encuadre horiozontal, "v" para encuadre
                vertical, o None para que el encuadre se elija automáticamente
                de modo que el dominio quede completamente contenido en la
                ventana.
        """
        if encuadre is not None and encuadre[0] not in "hv":
            raise ValueError(f"El encuadre '{encuadre}' no es válido.")
        
        if x_dominio is None:
            x_dominio = self.x_dominio
        if y_dominio is None:
            y_dominio = self.y_dominio
        
        # Desempaquetamos los componentes de los dominios
        izquierda, derecha = x_dominio
        abajo, arriba = y_dominio
        
        # Si no se especificó un encuadre, escogemos el que hace que el dominio
        # quede completamente contenido en la vista.
        if encuadre is None:
            if self.alto * (derecha - izquierda) >= self.ancho * (arriba - abajo):
                encuadre = "h"
            else:
                encuadre = "v"
        
        if encuadre[0] == "h":
            aux = arriba - abajo
            dv = self.alto * (derecha - izquierda) / self.ancho
            arriba = abajo + dv
            # Desplacamiento vertical para el centrado
            aux = (arriba - abajo - aux) / 2
            abajo -= aux
            arriba -= aux
        else:
            aux = derecha - izquierda
            dh = self.ancho * (arriba - abajo) / self.alto
            derecha = izquierda + dh
            # Desplacamiento horizontal para el centrado
            aux = (derecha - izquierda - aux) / 2 
            izquierda -= aux
            derecha -= aux
        
        self.ajustar_dominio((izquierda, derecha), (abajo, arriba))

    def vent_a_cart(self, p:tuple|PuntoCartesiano) -> PuntoCartesiano:
        r"""
        La pantalla está representada por pixeles, el pixel de arriba-izquierda
        tiene coordenadas (0,0), y el pixel de abajo-derecha tiene coordenadas
        (self.ancho - 1, self.alto - 1).

        Este método convierte las coordenadas de un píxel de la ventana, a su 
        correspondiente punto cartesiano en el dominio del plano.

        Así podemos tranformar de coordenadas de ventana a coordenadas
        cartesianas.

        Args:
            p (tuple|PuntoCartesiano): coordenadas de un pixel, no es necesario
                que el pixel tenga coordenadas enteras.
        """
        if isinstance(p, list|tuple):
            p = PuntoCartesiano(*p)
        x = self.x_dominio[0] + p.x * (self.x_dominio[1] - self.x_dominio[0]) / (self.ancho - 1)
        y = self.y_dominio[1] + p.y * (self.y_dominio[0] - self.y_dominio[1]) / (self.alto - 1)
        return PuntoCartesiano(x, y)

    def cart_a_vent(self, p:tuple|PuntoCartesiano) -> PuntoCartesiano:
        r"""
        Este método convierte las coordenadas de un punto cartesiano, a su 
        correspondiente pixel en la ventana. Las coordenadas devueltas no 
        necesariamente serán enteras.

        Así podemos tranformar de coordenadas cartesianas a coordenadas
        de ventana. 

        Args:
            p (tuple|PuntoCartesiano): coordenadas de un punto cartesiano.
        """
        if isinstance(p, list|tuple):
            p = PuntoCartesiano(*p)
        u = (p.x - self.x_dominio[0]) * (self.ancho - 1) / (self.x_dominio[1] - self.x_dominio[0])
        v = (p.y - self.y_dominio[1]) * (self.alto - 1) / (self.y_dominio[0] - self.y_dominio[1])
        return PuntoCartesiano(u, v)
    
    def distancia(self, p:tuple|PuntoCartesiano, q:tuple|PuntoCartesiano) -> float:
        r"""
        Calcula la distancia entre dos puntos, en este caso no importan 
        las unidades. Es decir, pueden ser pixeles, unidades cartesianas, etc.

        Args:
            p, q (tuple|PuntoCartesiano): puntos entre los que se calculará
                la distancia en linea recta.
            
        Returns:
            float: la distancia entrre los dos puntos dados.
        """
        if isinstance(p, list|tuple):
            p = PuntoCartesiano(*p)
        if isinstance(q, list|tuple):
            q = PuntoCartesiano(*q)
        return (q - p).magnitud()

    def dist_en_pixeles(self, p:tuple|PuntoCartesiano, q:tuple|PuntoCartesiano) -> float:
        r"""
        Calcula la distancia que hay en pixeles entre 2 puntos cartesianos,
        de acuerdo al mapeo que hay entre el área de dibujado y el dominio
        cartesiano que representa.

        Args:
            p, q (tuple|PuntoCartesiano): puntos cartesianos entre los que se
                calculará la separación en pixeles.
        
        Returns:
            float: separación en pixeles entre los puntos dados, el resultado
                no necesariamente es entero.
        """
        p = self.cart_a_vent(p)
        q = self.cart_a_vent(q)
        return self.distancia(p, q)

    def linea_vent(self, p:tuple|PuntoCartesiano, q:tuple|PuntoCartesiano, color:tuple|Color, ancho:float):
        r"""
        Recibe las cooredenadas de dos pixeles en la ventana y dibuja una 
        linea entre estos, del color y ancho especificado.

        Args:
            p, q (tuple|PuntoCartesiano): coordenadas de los pixeles entre
                los que se dibujará la linea.
            color (tuple|Color): color en forma de tupla (r, g, b).
            ancho (float): ancho de la linea en pixeles.
        """
        if isinstance(p, PuntoCartesiano):
            p = p.tupla()
        if isinstance(q, PuntoCartesiano):
            q = q.tupla()
        pygame.draw.line(self.ventana, color, p, q, ancho)

    def linea_cart(self, p:tuple|PuntoCartesiano, q:tuple|PuntoCartesiano, color:tuple|Color, ancho:float=1):
        r"""
        Recibe las cooredenadas de dos puntos cartesianos y dibuja una 
        linea entre estos, del color y ancho especificado.

        Args:
            p, q (tuple|PuntoCartesiano): coordenadas cartesianas de los puntos
                entre los que se dibujará la linea.
            color (tuple|Color): color en forma de tupla (r, g, b).
            ancho (float): ancho de la linea en pixeles.
        """
        p = self.cart_a_vent(p)
        q = self.cart_a_vent(q)
        self.linea_vent(p, q, color, ancho)
    
    def circulo_vent(self, centro:tuple|PuntoCartesiano, radio:float, color:tuple|Color, ancho=0):
        r"""
        Dibuja un circulo del colo especificado centrado en `centro`, el cual 
        contiene las coordenadas de un pixel. El `radio` está dado en pixeles.
        Si el ancho es mayor que cero, entonces solo se dibujará el contorno
        del circulo, pero si es cero entonces se dibujará el circulo relleno.

        Args:
            centro (tuple|PuntoCartesiano): coordenadas del pixel que será el
                centro del circulo.
            radio (float): radio del circulo en pixels.
            color (tuple|Color): color en forma de tupla (r, g, b).
            ancho (float): ancho del borde en pixeles.
        """
        if isinstance(centro, PuntoCartesiano):
            centro = centro.tupla()
        pygame.draw.circle(self.ventana, color, centro, radio, ancho)
    
    def circulo_cart(self, centro:tuple|PuntoCartesiano, radio:float, color:tuple|Color, ancho=0):
        r"""
        Dibuja un circulo del colo especificado centrado en `centro`, el cual 
        contiene las coordenadas cartesianas de un punto. El `radio` está dado 
        en unidades cartesianas.
        Si el ancho es mayor que cero, entonces solo se dibujará el contorno
        del circulo, pero si es cero entonces se dibujará el circulo relleno.

        Args:
            centro (tuple|PuntoCartesiano): coordenadas cartesianas del centro 
                del circulo.
            radio (float): radio del circulo en unidades cartesianas.
            color (tuple|Color): color en forma de tupla (r, g, b).
            ancho (float): ancho del borde en pixeles.
        """
        if isinstance(centro, tuple|list):
            centro = PuntoCartesiano(*centro)
        centro_vent = self.cart_a_vent(centro)
        radio_vent = self.cart_a_vent(centro + (radio, 0)).x - centro_vent.x
        self.circulo_vent(centro_vent, math.ceil(radio_vent), color, ancho)

    def punto(self, p, color:tuple|Color, tamano:float=3):
        r"""
        Dibuja un punto las coordenadas cartesianas especificadas en `p`. 
        El tamaño del punto está dado en pixeles y representa el radio del
        punto.

        Args:
            p (tuple|PuntoCartesiano): coordenadas del punto cartesiano.
            color (tuple|Color): color en forma de tupla (r, g, b).
            tamano (float): tamaño o radio del punto en pixeles.
        """
        coord_vent = self.cart_a_vent(p)
        self.circulo_vent(coord_vent, tamano, color)

    def dibujar_ejes(self, color:tuple|Color=Color.NEGRO, ancho=1):
        r"""
        Dibuja los ejes del plano cartesiano en el color y ancho especificados.

        Si `self.ejes` es False, entonces no se dibujará nada.

        Args:
            color (tuple|Color): color en forma de tupla (r, g, b).
            ancho (float): ancho de los ejes en pixeles.
        """
        # x ejes
        inicio = (self.x_dominio[0], 0)
        fin = (self.x_dominio[1], 0)
        self.linea_cart(inicio, fin, color, ancho=1)

        # y ejes
        inicio = (0, self.y_dominio[0])
        fin = (0, self.y_dominio[1])
        self.linea_cart(inicio, fin, color, ancho=1)

    def dibujar_marcas(self, color=Color.NEGRO, ancho=1):
        r"""
        Los ejes pueden llevar marcas. Esta función los dibuja, la separación
        entre cada marca está definida por `self.marcas_sep` y está dada
        en unidades cartesianas. Las marcas tiene una longtitud total de 
        7 pixeles.

        Si `self.marcas_sep` es None, entonces no se dibujará nada.

        Args:
            color (tuple|Color): color en forma de tupla (r, g, b).
            ancho (float): ancho de las marcas en pixeles.
        """
        if self.marcas_sep is None:
            return
        # Draw marks in the x-ejes
        x = math.ceil(self.x_dominio[0] / self.marcas_sep) * self.marcas_sep
        while x <= self.x_dominio[1]:
            p_x = self.cart_a_vent((x, 0))
            inicio = p_x + (0, -3)
            fin = p_x + (0, 3)
            self.linea_vent(inicio, fin, color, ancho)
            x += self.marcas_sep
        
        # Draw marks in the y-ejes
        y = math.ceil(self.y_dominio[0] / self.marcas_sep) * self.marcas_sep
        while y <= self.y_dominio[1]:
            p_y = self.cart_a_vent((0, y))
            inicio = p_y + (-3, 0)
            fin = p_y + (3, 0)
            self.linea_vent(inicio, fin, color, ancho)
            y += self.marcas_sep
    
    def dibujar_cuadricula(self, color=Color.GRIS_CLARO, ancho=1):
        r"""
        Dibuja una cuadricula, donde cada linea de esta tendrá una separación
        que está definida por `self.marcas_sep` y está dada en unidades
        cartesianas.

        Si `self.marcas_sep` es None o `self.cuadricula` es False, entonces 
        no se dibujará nada.

        Args:
            color (tuple|Color): color en forma de tupla (r, g, b).
            ancho (float): ancho de las lineas en pixeles.
        """
        if self.marcas_sep is None:
            return
        
        # Draw marks in the x-ejes
        x = math.ceil(self.x_dominio[0] / self.marcas_sep) * self.marcas_sep
        while x <= self.x_dominio[1]:
            inicio = (x, self.y_dominio[0])
            fin = (x, self.y_dominio[1])
            self.linea_cart(inicio, fin, color, ancho)
            x += self.marcas_sep
        
        # Draw marks in the y-ejes
        y = math.ceil(self.y_dominio[0] / self.marcas_sep) * self.marcas_sep
        while y <= self.y_dominio[1]:
            inicio = (self.x_dominio[0], y)
            fin = (self.x_dominio[1], y)
            self.linea_cart(inicio, fin, color, ancho)
            y += self.marcas_sep

    def iniciar(self):
        r"""
        Esta función inicia el ciclo principal de dibujado de la escena.
        La idea es heredar de esta clase para extender la escena que será 
        dibujada.

        El método `self.dibujar_pre_escena` debe sobre-escribirse para dibujar
        los elementos que irán detrás de los elementos predefinidos como son
        los ejes, marcas y cuadrícula.

        El método `self.dibujar_escena` debe sobre-escribirse para dibujar
        los elementos que irán delante de los elementos predefinidos.
        """
        while True:
            # Procesamos los eventos de nuestro interés
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Si se cerró la ventana: salimos
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Si se apretó el click izquierdo: empezamos a monitorear
                        # el arrastre.
                        self.arrastrando = True
                        self.mouse_pos = PuntoCartesiano(*event.pos)
                    elif event.button == 4:
                        # Si hubo scroll hacia arriba: reducimos el dominio
                        # un 10%, en 'x' si CTRL no está presionado y en 'y'
                        # si ALT no está presionado.
                        x_dominio = self.x_dominio
                        y_dominio = self.y_dominio
                        if not self.ctrl:
                            x_dominio = (x_dominio[0] / 1.1, x_dominio[1] / 1.1)
                        if not self.alt:
                            y_dominio = (y_dominio[0] / 1.1, y_dominio[1] / 1.1)
                        self.ajustar_dominio(x_dominio, y_dominio)
                    elif event.button == 5:
                        # Si hubo scroll hacia abajo: aumentamos el dominio
                        # un 10%, en 'x' si CTRL no está presionado y en 'y'
                        # si ALT no está presionado.
                        x_dominio = self.x_dominio
                        y_dominio = self.y_dominio
                        if not self.ctrl:
                            x_dominio = (x_dominio[0] * 1.1, x_dominio[1] * 1.1)
                        if not self.alt:
                            y_dominio = (y_dominio[0] * 1.1, y_dominio[1] * 1.1)
                        self.ajustar_dominio(x_dominio, y_dominio)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        # Si se liberó el click izquierdo: dejamos de monitorear
                        # el arrastre.
                        self.arrastrando = False
                        self.mouse_pos = None
                elif event.type == pygame.MOUSEMOTION:
                    # Si se movió el mouse: desplazamos el dominio completo
                    # solo si está siendo presionado el clicl izquierdo.
                    if self.arrastrando:
                        mov = -self.mouse_pos + event.pos
                        pix_origen = self.cart_a_vent((0,0))
                        cart_mov = self.vent_a_cart(pix_origen + mov)
                        x_dominio = (self.x_dominio[0] - cart_mov.x, self.x_dominio[1] - cart_mov.x)
                        y_dominio = (self.y_dominio[0] - cart_mov.y, self.y_dominio[1] - cart_mov.y)
                        self.ajustar_dominio(x_dominio, y_dominio)
                        self.mouse_pos = PuntoCartesiano(*event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        # Si se preisonó la tecla CTRL
                        self.ctrl = True
                    elif event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                        # Si se preisonó la tecla ALT
                        self.alt = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        # Si se liberó la tecla CTRL
                        self.ctrl = False
                    elif event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                        # Si se liberó la tecla ALT
                        self.alt = False

            # Primero rellenamos la ventana con el color de fondo.
            self.ventana.fill(self.color_fondo)
            
            # Dibujamos los elementos que van detrás de los
            # elementos predefinidos.
            self.dibujar_pre_escena()

            # Dibujamos los elementos predefinidos, solo si fueron requeridos.
            if self.cuadricula:
                self.dibujar_cuadricula()
            if self.ejes:
                self.dibujar_ejes()
            if self.marcas_sep is not None:
                self.dibujar_marcas()

            # Dibujamos los elementos que van delante de los
            # elementos predefinidos.
            self.dibujar_escena()
            
            # Mandamos la escena a la pantalla
            pygame.display.flip()
            
            # Cada que haya un cambio de segundo, mostramos 
            # una aproximación muy burda de los FPS.
            if int(self.tiempo) < int(time.time()):
                print(f"FPS: {1 / (time.time() - self.tiempo)}")
            
            # Actualizamos el tiempo
            self.tiempo = time.time()
    
    def dibujar_pre_escena(self):
        r"""
        Este método se debe sobre-escribir en las subclases y su función es
        dibujar los elementos que serán puestos detrás de los elementos 
        predefinidos.
        """
        pass

    def dibujar_escena(self, *args):
        r"""
        Este método se debe sobre-escribir en las subclases y su función es
        dibujar los elementos que serán puestos delante de los elementos 
        predefinidos.
        """
        pass
#




if __name__ == "__main__":
    ventana = PlanoCartesiano(Color.BLANCO, 1000, 800, (-20, 20), (-20, 20))
    ventana.iniciar()
