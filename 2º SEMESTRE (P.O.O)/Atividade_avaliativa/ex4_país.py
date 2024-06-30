# EXERCÍCIO 4
# Escreva uma classe que represente um país. Um país é representado através dos atributos: código ISO 3166-1 (ex.: BRA), nome (ex.: Brasil),
# população (ex.: 193.946.886) e a sua dimensão em Km2 (ex.: 8.515.767,049). Além disso, cada país mantém uma lista de outros países com os
# quais ele faz fronteira. Escreva a classe em Python e forneça os seus membros a seguir:
# a) Construtor que inicialize o código ISO, o nome e a dimensão do país;
# b) Métodos de acesso (getter/setter) para as propriedades código ISO, nome, população e dimensão do país;
# c) Um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica). Dois países são iguais se tiverem o mesmo código ISO;
# d) Um método que informe se outro país é limítrofe do país que recebeu a mensagem;
# e) Um método que retorna a densidade populacional do país;
# f) Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países.
# g) Escreva código de teste que instancie objetos de exemplo e demonstre as capacidades da classe
# -------------------------------------------------------------------------------------------------------------------------------------------------------

class Pais:
    def __init__(self, codigo:str, nome:str, população:int, dimensao:float, fronteiras:list[str]):
        self.__codigo = codigo
        self.__nome = nome
        self.__população = população
        self.__dimensao = dimensao
        self.__fronteiras = fronteiras

# Getter e Setter
# Código
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

# Nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

# População
    @property
    def população(self):
        return self.__população
    
    @população.setter
    def população(self, população):
        self.__população = população

# Dimensão
    @property
    def dimensao(self):
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao):
        self.__dimensao = dimensao

# Fronteira
    @property
    def fronteiras(self):
        return self.__fronteiras
    
    @fronteiras.setter
    def fronteiras(self, fronteiras):
        self.__fronteiras = fronteiras

# Comparar países
    def comparar_pais(self, pais):
        return pais.codigo == self.codigo
    
# Saber país limítrofe (de fronteira)
    def limitrofe(self, pais):
        return pais.codigo in self.fronteiras

# Densidade Populacional
    def densidade_populacional(self):
        return self.população / self.pais

# Lista de vizinhos
    def vizinhos_comuns(self, pais):
        vizinhos_em_comum = []
        for vizinho in self.fronteiras:
            if vizinho in pais.fronteiras:
                vizinhos_em_comum.append(vizinho)
        return vizinhos_em_comum

# Testes
def verificar():
    pais1 = Pais(codigo = "ESP", nome = "Espanha", população = 48085361, dimensao = 505983.2, fronteiras = ["FRA", "POR", "GBR", "MAR"])
    pais2 = Pais(codigo = "GBR", nome = "Reino Unido", população = 63181775, dimensao = 130279.2, fronteiras = ["FRA", "CHE", "AUT", "SVN"])

    vizinhos_comuns = pais1.vizinhos_comuns(pais2)
    print(vizinhos_comuns)

verificar()
