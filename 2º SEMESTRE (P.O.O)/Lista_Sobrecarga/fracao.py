import math

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("O denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplifica()

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def simplifica(self):
        mdc = math.gcd(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc

        if self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador

    # soma de frações
    def __add__(self, outra):
        novo_numerador = self.numerador * outra.denominador + outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        resultado = Fracao(novo_numerador, novo_denominador)
        resultado.simplifica()
        return resultado
    
    # subtração de frações
    def __sub__(self, outra):
        novo_numerador = self.numerador * outra.denominador - outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        resultado = Fracao(novo_numerador, novo_denominador)
        resultado.simplifica()
        return resultado

    # multiplicação de frações
    def __mul__(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        resultado = Fracao(novo_numerador, novo_denominador)
        resultado.simplifica()
        return resultado

    # divisão de frações
    def __truediv__(self, outra):
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        resultado = Fracao(novo_numerador, novo_denominador)
        resultado.simplifica()
        return resultado

# Testes

f1 = Fracao(5, 20)
f2 = Fracao(3, 27)

print(f"Fração 1: {f1}")
print(f"Fração 2: {f2}")

soma = f1 + f2
print(f"Soma: {soma}")
subtracao = f1 - f2
print(f"Subtração: {subtracao}")
multiplicacao = f1 * f2
print(f"Multiplicação: {multiplicacao}")
divisao = f1 / f2
print(f"Divisão: {divisao}")
