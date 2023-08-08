class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print(f"Coordenadas: ({self.x}, {self.y})")



punto1 = Punto(3, 5)
punto1.mostrar_coordenadas()

punto2 = Punto(-2, 7)
punto2.mostrar_coordenadas()