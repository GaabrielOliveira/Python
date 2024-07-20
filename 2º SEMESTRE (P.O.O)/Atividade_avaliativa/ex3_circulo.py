# EXERCÍCIO 3
# Escreva em Python uma classe Circulo, que representa um círculo no plano cartesiano. Forneça os seguintes membros de classe:
# a) Um construtor que receba o raio e um ponto (o ponto do círculo). O parâmetro ponto deve ser do tipo Ponto2D criado anteriormente.
# b) Métodos de acesso ao atributo raio do círculo
# c) Métodos inflar e desinflar, que, respectivamente, aumentam e diminuem o raio do círculo de um dado valor
# d) Método mover, que recebe um ponto por parâmetro, que:
# • caso o ponto não seja passado, leva o círculo para a origem do espaço 2D, isto é, ponto (0, 0)
# • caso o ponto seja passado, move o círculo para o ponto indicado pelo parâmetro
# e) Método que retorna a área do círculo
# Escreva código de teste que instancie objetos de exemplo e demonstre as capacidades da classe.
# -------------------------------------------------------------------------------------------------------------------------------------------------------

from ex2_ponto2d import Ponto2D
from math import pi

class Circulo:
    def __init__(self, raio, centro):
        self._raio = raio
        self._centro = centro
    
# Get e Set
    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, value):
        self._raio = value
    
# Inflar e Desinflar
    def inflar(self, value):
        self._raio += value

    def desinflar(self, value):
        if value > self._raio:
            print("Erro!")
            return
        self._raio -= value

# Mover
    def mover(self, novo_centro = None):
        if novo_centro is None:
            self._centro = Ponto2D(0.0, 0.0)
        else:
            self._centro = novo_centro

# Area
    def area(self):
        return self._raio**2 * pi
    
    def __str__(self):
        return f"raio = {self._raio}, centro = {self._centro}"

# # Teste
def teste_get_e_set():
    # Criando pontos
    centro1 = Ponto2D(1.0, 1.0)
    centro2 = Ponto2D(3.0, 4.0)

    # Criando círculos
    circulo1 = Circulo(5.0, centro1)
    circulo2 = Circulo(10.0, centro2)

    # Testando getters e setters
    print(f"Circulo 1: {circulo1}")
    print(f"Circulo 2: {circulo2}")

    circulo1.raio = 6.0
    print(f"Novo Circulo 1: {circulo1}")

    # Testando inflar e desinflar
    circulo1.inflar(2)
    print(f"Circulo 1 inflado: {circulo1}")

    circulo1.desinflar(3)
    print(f"Circulo 1 desinflado: {circulo1}")

    # Testando o método mover
    circulo1.mover()
    print(f"Circulo 1 movido para a origem: {circulo1}")

    circulo1.mover(Ponto2D(2.0, 2.0))
    print(f"Circulo 1 movido para (2.0, 2.0): {circulo1}")

    # Testando a área do círculo
    area_circulo1 = circulo1.area()
    print(f"Área do Circulo1: {area_circulo1:.2f}")

# def verificacao_ex3():
teste_get_e_set()


