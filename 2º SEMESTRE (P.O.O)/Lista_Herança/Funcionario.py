class Funcionario:
    def __init__(self, nome:str, cpf:str, salario:float, departamento:str):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento
    
    def bonificar(self):
        self.salario += self.salario * 0.10
        return self.salario


class Gerente(Funcionario):
    def __init__(self, nome:str, cpf:str, salario:float, departamento:str,senha:int, numero_func:int):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.numero_func = numero_func
    
    def autenticar_senha(self, senha):
        return self.senha == senha

    def bonificar(self):
        self.salario += self.salario * 0.15
        return self.salario

# Testes:
funcionario = Funcionario("Gabriel Felipe", "123.456.789-00", 5000, "Financeiro")

gerente = Gerente("Barbara Silva", "987.654.321-00", 8000, "TI", "1123785946", 10)

print(f"Salário de {funcionario.nome} antes da bonificação: R$ {5000}")
print(f"Salário de {funcionario.nome} após bonificação: R$ {funcionario.bonificar()}")

print(f"Salário de {gerente.nome} antes da bonificação: R$ {8000}")
print(f"Salário de {gerente.nome} após bonificação: R$ {gerente.bonificar()}")

print(f"Autenticação de senha correta para {gerente.nome}: {gerente.autenticar_senha('1123785946')}")
print(f"Autenticação de senha incorreta para {gerente.nome}: {gerente.autenticar_senha('senha_errada')}")
        