class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        distancia = ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)**0.5
        return distancia



punto1 = Punto(3, 5)
punto1.mostrar()

punto2 = Punto(-2, 7)
punto2.mostrar()

distancia = punto1.calcular_distancia(punto2)
print(f"Distancia entre los puntos: {distancia}")

punto1.mover(1, -2)
punto1.mostrar()