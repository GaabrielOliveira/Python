s = "uma string qualquer"
print(s)
    # a saída seria 'uma string qualquer'
type(s)
    # a saída seria <class 'str'>
# ------------------------
s = 1
type(s)
    # a saída seria <class 'int'>

# ====================================================

class Pessoa :
	pass   # não faça nada

p = Pessoa()  # instanciação da classe
print(type(p))

    # <class '__main__.Pessoa'>

# ====================================================

class Pessoa :
	def __init__(self, nome, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome
# --------------------------------------
p1 = Pessoa("Fulano", "da Silva")
p2 = Pessoa("Ciclano", "de Souza")

# ====================================================