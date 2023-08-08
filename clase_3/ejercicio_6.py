class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class Pinta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PICAS = "Picas"

# Ejemplo de uso
carta1 = Carta(7, Pinta.CORAZONES)
carta2 = Carta(10, Pinta.PICAS)

print("Carta 1:", carta1.valor, carta1.pinta)
print("Carta 2:", carta2.valor, carta2.pinta)