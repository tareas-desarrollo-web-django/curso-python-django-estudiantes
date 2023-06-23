import sys
import pygame
import math
import time
from random import randint
from copy import deepcopy
from exercise import PuntoCartesiano


# Colors
class Colors:
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    lightgray = (240, 240, 240)
    gray = (200, 200, 200)


class Graphics:
    def __init__(self, bg_color, width, height, x_range, y_range) -> None:
        # Initialize the elements of the pygame library
        pygame.init()

        # Background color
        self.bg_color = bg_color
        # Width of and height of the drawing area
        self.width = width
        self.height = height
        # In ordet to draw elements as if we are in a cartesian space,
        # the drawing area is maped into a cartesian domain:
        #   x_range=(x_0,x1) defines the x interval of the domain
        #   y_range=(y_0,y1) defines the y interval of the domain
        self.x_range = None
        self.y_range = None

        # Predefined elements configuration
        self.axis = True
        self.marks_sep = 1
        self.grid = True

        # Safely set the domain
        self.set_domain(x_range, y_range)

        # Window where we will draw
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def set_domain(self, x_range, y_range):
        if x_range is None or y_range is None:
            raise ValueError("Ranges can't be None")
        
        self.x_range = deepcopy(x_range)
        self.y_range = deepcopy(y_range)
        # Make sure that x_0 < x_1 and y_0 < y_1
        if self.x_range[1] < self.x_range[0]:
            self.x_range = (self.x_range[1], self.x_range[0])
        if self.y_range[1] < self.y_range[0]:
            self.y_range = (self.y_range[1], self.y_range[0])
    
    def set_domain_proportional(self, x_range, y_range, side=None):
        '''side: "h"=horizontal, "v"=vertical'''
        left, right = x_range
        bottom, top = y_range
        
        # Of no side chosen, chose the one that makes the domain fit inside the view
        if side is None:
            if self.height * (right - left) >= self.width * (top - bottom):
                side = "h"
            else:
                side = "v"
        
        if side[0] == "h":
            # Auxiliary for centering the box
            aux = top - bottom
            dv = self.height * (right - left) / self.width
            top = bottom + dv
            # The vertical offset for the centering.
            aux = (top - bottom - aux) / 2
            bottom -= aux
            top -= aux
        else:
            # Auxiliary for centering the box
            aux = right - left
            dh = self.width * (top - bottom) / self.height
            right = left + dh
            # The horizontal offset for the centering
            aux = (right - left - aux) / 2 
            left -= aux
            right -= aux
        
        self.set_domain((left, right), (bottom, top))

    def screen_to_cart(self, p:tuple|list):
        x = self.x_range[0] + p[0] * (self.x_range[1] - self.x_range[0]) / (self.width - 1)
        y = self.y_range[1] + p[1] * (self.y_range[0] - self.y_range[1]) / (self.height - 1)
        return x, y

    def cart_to_screen(self, p:tuple|list):
        u = (p[0] - self.x_range[0]) * (self.width - 1) / (self.x_range[1] - self.x_range[0])
        v = (p[1] - self.y_range[1]) * (self.height - 1) / (self.y_range[0] - self.y_range[1])
        return u, v
    
    def dist(self, p0, p1):
        return math.sqrt((p1[0] - p0[0]) * (p1[0] - p0[0]) + (p1[1] - p0[1]) * (p1[1] - p0[1]))

    def dist_cart_to_screen(self, p0, p1):
        p0 = self.cart_to_screen(p0)
        p1 = self.cart_to_screen(p1)
        return self.dist(p0, p1)

    def draw_cart_line(self, color, start, end, width=1):
        start = self.cart_to_screen(start)
        end = self.cart_to_screen(end)
        pygame.draw.line(self.screen, color, start, end, width)
    
    def draw_cart_circle(self, color, center, radius, width=0):
        '''radius is given in pixels, ¿should it be given in cartesian 
        units instead? ¿maybe both should be supported?'''
        center = self.cart_to_screen(center)
        pygame.draw.circle(self.screen, color, center, radius, width)

    def draw_axis(self, color=Colors.black, width=1):
        # x axis
        start = (self.x_range[0], 0)
        end = (self.x_range[1], 0)
        self.draw_cart_line(color, start, end, width=1)

        # y axis
        start = (0, self.y_range[0])
        end = (0, self.y_range[1])
        self.draw_cart_line(color, start, end, width=1)

    def draw_marks(self, color=Colors.black, width=1):
        if self.marks_sep is None:
            return
        # Draw marks in the x-axis
        x = math.ceil(self.x_range[0] / self.marks_sep) * self.marks_sep
        while x <= self.x_range[1]:
            u, v = self.cart_to_screen((x, 0))
            start = (u, v - 3)
            end = (u, v + 3)
            pygame.draw.line(self.screen, color, start, end, width)
            x += self.marks_sep
        
        # Draw marks in the y-axis
        y = math.ceil(self.y_range[0] / self.marks_sep) * self.marks_sep
        while y <= self.y_range[1]:
            u, v = self.cart_to_screen((0, y))
            start = (u - 3, v)
            end = (u + 3, v)
            pygame.draw.line(self.screen, color, start, end, width)
            y += self.marks_sep
    
    def draw_grid(self, color=Colors.lightgray, width=1):
        # Draw marks in the x-axis
        x = math.ceil(self.x_range[0] / self.marks_sep) * self.marks_sep
        while x <= self.x_range[1]:
            start = (x, self.y_range[0])
            end = (x, self.y_range[1])
            self.draw_cart_line(color, start, end, width)
            x += self.marks_sep
        
        # Draw marks in the y-axis
        y = math.ceil(self.y_range[0] / self.marks_sep) * self.marks_sep
        while y <= self.y_range[1]:
            start = (self.x_range[0], y)
            end = (self.x_range[1], y)
            self.draw_cart_line(color, start, end, width)
            y += self.marks_sep

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            
            # Draw before the predefined elements
            self.draw_pre_scene()

            # Predefined elements
            if self.grid:
                self.draw_grid()
            if self.axis:
                self.draw_axis()
            if self.marks_sep is not None:
                self.draw_marks()

            # Draw after the predefined elements
            self.draw_scene()
            
            pygame.display.flip()
            
            # Update the time
            if int(self.time) < int(time.time()):
                print(f"FPS: {1 / (time.time() - self.time)}")
            self.time = time.time()
    
    def draw_pre_scene(self):
        pass

    def draw_scene(self, *args):
        pass
#

class CartesianPlane(Graphics):
    def __init__(self, bg_color, width, height, x_range, y_range) -> None:
        super().__init__(bg_color, width, height, x_range, y_range)
        self.set_domain_proportional(x_range, y_range)

        self.orbits = []
        for _ in range(10):
            ox = randint(int(self.x_range[0] + 10), int(self.x_range[1] - 10))
            oy = randint(int(self.y_range[0] + 10), int(self.y_range[1] - 10))
            px = ox + randint(-10, 10)
            py = oy + randint(-10, 10)
            origin = (ox, oy)
            point = (px, py)
            # Grados a girar por cada segundo
            t = randint(20, 200)
            orbit_radius = self.dist_cart_to_screen(origin, point)
            self.orbits.append({"point":PuntoCartesiano(*point), "origin":origin, "angle":t, "orbit_radius":orbit_radius})
        
        self.time = time.time()
    #

    def draw_pre_scene(self):
        return
        for orbit in self.orbits:
            self.draw_cart_circle(Colors.gray, orbit["origin"], orbit["orbit_radius"], 1)
    
    def draw_scene(self):
        dt = time.time() - self.time
        for orbit in self.orbits:
            point = (orbit["point"].x, orbit["point"].y)
            self.draw_cart_line(Colors.blue, orbit["origin"], point, 2)
            self.draw_cart_circle(Colors.black, orbit["origin"], 3)
            self.draw_cart_circle(Colors.red, point, 3)

            orbit["point"].rotar_general(orbit["angle"] * dt, orbit["origin"])
#


if __name__ == "__main__":
    window = CartesianPlane(Colors.white, 1000, 800, (-20, 20), (-20, 20))
    window.run()
