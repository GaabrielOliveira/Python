class FormaGeometrica:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

    def calcula_area(self):
        pass

    def calcula_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcula_area(self):
        self.area = self.base * self.altura
        return self.area

    def calcula_perimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        return self.perimetro

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcula_area(self):
        # Usando a fórmula de Herão para calcular a área do triângulo
        semi_perimetro = (self.lado1 + self.lado2 + self.lado3) / 2  # semiperímetro
        self.area = (semi_perimetro * (semi_perimetro - self.lado1) * (semi_perimetro - self.lado2) * (semi_perimetro - self.lado3)) ** 0.5
        return self.area

    def calcula_perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        return self.perimetro


# Testes:
retangulo = Retangulo(5, 10)
triangulo = Triangulo(3, 4, 5)

print(isinstance(retangulo, FormaGeometrica)) 
print(isinstance(triangulo, FormaGeometrica))

print(f"Área do Retângulo: {retangulo.calcula_area()}")
print(f"Área do Triângulo: {triangulo.calcula_area()}")

print(f"Perimetro do Retângulo: {retangulo.calcula_perimetro()}")
print(f"Perimetro do Triângulo: {triangulo.calcula_perimetro()}")