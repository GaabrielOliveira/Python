class Pessoa:
# construtor da classe
    def __init__(self, nome, sobrenome, ano_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc
# métodos
    def nome_completo(self):
        result = self.nome + " " + self.sobrenome
        return result

    def idade(self):
        result = 2024 - self.ano_nasc
        return result


# SIMPLIFICADO:
    
    # def nome_completo(self):
    #     return self.nome + " " + self.sobrenome

    # def idade(self):
    #     return 2024 - self.ano_nasc
    
# ------------------------------------------------------------

#  nome completo = nome + sobrenome
#  idade = ano atual - ano de nascimento