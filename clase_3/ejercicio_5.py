
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia_centro_punto <= self.radio


centro = Punto(0, 0)
circulo = Circulo(centro, 5)

print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())

punto_1 = Punto(3, 4)
punto_2 = Punto(6, 8)

print("Punto 1 pertenece al círculo:", circulo.punto_pertenece(punto_1))
print("Punto 2 pertenece al círculo:", circulo.punto_pertenece(punto_2))