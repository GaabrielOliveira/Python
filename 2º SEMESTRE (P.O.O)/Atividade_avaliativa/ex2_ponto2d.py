# EXERCÍCIO 2
# Escreva em Python uma classe Ponto2D que represente um ponto no plano
# cartesiano. A classe deve ter os parâmetros que representam abcissa e ordenada, isto é, o valor de X e Y do ponto. A classe também deve oferecer os
# seguintes membros:
# a) Construtor que permita a inicialização do ponto:
# • Por default (sem parâmetros) na origem do espaço 2D
# • Num local indicado por dois parâmetros do tipo float (indicando o valor de abcissa e ordenada do ponto que está sendo criado);
# b) Métodos de acesso (getter/setter) dos atributos do ponto
# c) Método denominado compara, que recebe um Ponto2D como parâmetro e retorna verdadeiro caso sejam o mesmo ponto, ou falso,caso contrário
# d) Método de representação do objeto como string
# e) Método que permita calcular a distância do ponto do objeto, para outro ponto recebido como parâmetro
# f) Método clone, que retorna uma nova instância de um ponto no mesmo local do objeto.
# g) Escreva código de teste que instancie objetos de exemplo e demonstre as capacidades da classe.
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import math
class Ponto2D:
    # Contrutor:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y

# Get e Set de X:
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

# Get e Set de Y:
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
    
# Função de comparação:
    def compara(self, novo_ponto):
        if (self.__x == novo_ponto.x and self.__y == novo_ponto.y):
            return True # ou 1
        else:
            return False # ou 0
    
# Representação como string:
    def __str__(self):
        return f'\nX:({self.__x}) \nY:({self.__y})\n'

# Calculando os pontos:
    def dist(x2, y2, x1, y1):
        a = (x2 - x1)**2 + (y2 - y1)**2
        b = math.sqrt(a)
        return b

# Clone:
    def clone (self):
        return Ponto2D(self.__x, self.__y)
    
# Testes:
# def teste():
#     p1 = Ponto2D()
#     p2 = Ponto2D(3.8 , 4.0)
#     print(f'p1:{p1}')
#     print(f'p2:{p2}')

#     p1.x = 3.6
#     p1.y = 1.7
#     print(f'p1 atualizado: {p1}')

#     p2.x = 3.9
#     p2.y = 2.5
#     print(f'p2 atualizado: {p2}')

# teste()

