import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

circulo1 = Circulo(5)
circulo2 = Circulo(10)

print(f"Área del círculo 1 (radio 5): {circulo1.calcular_area():.2f}")
print(f"Área del círculo 2 (radio 10): {circulo2.calcular_area():.2f}")