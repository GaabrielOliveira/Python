class FormaGeometrica:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

    def calc_area(self):
        pass

    def calc_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calc_area(self):
        self.area = self.base * self.altura
        return self.area

    def calc_perimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        return self.perimetro

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calc_area(self):
        semiperimetro = (self.lado1 + self.lado2 + self.lado3) / 2
        self.area = (semiperimetro * (semiperimetro - self.lado1) * (semiperimetro - self.lado2) * (semiperimetro - self.lado3)) ** 0.5
        return self.area

    def calc_perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        return self.perimetro


# Testes:
retangulo = Retangulo(5, 10)
triangulo = Triangulo(3, 4, 5)

print(isinstance(retangulo, FormaGeometrica)) 
print(isinstance(triangulo, FormaGeometrica))

print(f"Área do Retângulo: {retangulo.calc_area()}")
print(f"Área do Triângulo: {triangulo.calc_area()}")

print(f"Perimetro do Retângulo: {retangulo.calc_perimetro()}")
print(f"Perimetro do Triângulo: {triangulo.calc_perimetro()}")