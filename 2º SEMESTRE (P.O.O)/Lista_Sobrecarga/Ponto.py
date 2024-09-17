class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Soma
    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)
    
    # Subtração
    def __sub__(self, outro):
        return Ponto(self.x - outro.x, self.y - outro.y)
    
    # Multiplicação
    def __mul__(self, outro):
        if isinstance(outro, Ponto):
            return self.x * outro.x + self.y * outro.y
        else:
            raise TypeError("A multiplicação só pode ser feita entre dois objetos do tipo Ponto.")
    
    def __rmul__(self, escalar):
        return Ponto(escalar * self.x, escalar * self.y)


# Testes

p1 = Ponto(3, 4)
p2 = Ponto(1, 2)

print(f"Ponto 1: {p1}")
print(f"Ponto 2: {p2}")

p3 = p1 + p2
print(f"Soma de P1 + P2: {p3}")

p4 = p1 - p2
print(f"Subtração de P1 - P2: {p4}")

produto_escalar = p1 * p2
print(f"Produto escalar de P1 * P2: {produto_escalar}")

p5 = 3 * p1
print(f"Multiplicação de 3 * P1: {p5}")
