
import math

class PuntoCartesiano:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotar(self, t):
        g = t * math.pi / 180
        x_aux = math.cos(g) * self.x - math.sin(g) * self.y
        y_aux = math.sin(g) * self.x + math.cos(g) * self.y
        self.x = round(x_aux, 5)
        self.y = round(y_aux, 5)

if __name__ == "__main__":
    p = PuntoCartesiano(1, 0)


