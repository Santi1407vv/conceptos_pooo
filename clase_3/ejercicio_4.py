class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, esquina_superior_izquierda, esquina_inferior_derecha):
        self.esquina_superior_izquierda = esquina_superior_izquierda
        self.esquina_inferior_derecha = esquina_inferior_derecha

    def calcular_perímetro(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return 2 * (base + altura)

    def calcular_área(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return base == altura



punto_superior_izquierdo = Punto(1, 5)
punto_inferior_derecho = Punto(7, 1)

rectangulo = Rectángulo(punto_superior_izquierdo, punto_inferior_derecho)

print("Perímetro:", rectangulo.calcular_perímetro())
print("Área:", rectangulo.calcular_área())

if rectangulo.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")