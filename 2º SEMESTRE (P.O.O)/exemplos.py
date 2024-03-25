class Pessoa :
	def __init__(self, nome, sobrenome, ano_nasc):
		self.__nome = nome
		self.sobrenome = sobrenome
		self.ano_nasc = ano_nasc
# --------------------------------------
def getNome(self):
    return self.__nome

def setNome(self, novo_nome : str):
    if (len(novo_nome) >= 2): 
        self.__nome = novo_nome            


def nome_completo(self):
    result = self.__nome + " " + self.sobrenome
    return result

def idade(self):
    result = 2024 - self.ano_nasc
    return result

p1 = Pessoa("Fulano", "da Silva", 2002)
p2 = Pessoa("Ciclano", "de Souza", 2005)
p3 = Pessoa(nome="Zezinho", sobrenome="Silva", ano_nasc=2004)


print(p3.nome_completo())
print(p3.idade())

# com os parametros nomeados pode mudar a ordem.