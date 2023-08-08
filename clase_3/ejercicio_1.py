class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def mostrar_información(self):
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
        print(f"Kilometraje: {self.kilometraje} km")



mi_auto = Vehículo(200, 50000)
mi_auto.mostrar_información()