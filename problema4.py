class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

rectangulo = Rectangulo(4, 6)
print(f"Área del rectángulo (4x6): {rectangulo.calcular_area()}")

cuadrado = Cuadrado(5)
print(f"Área del cuadrado (lado 5): {cuadrado.calcular_area()}")