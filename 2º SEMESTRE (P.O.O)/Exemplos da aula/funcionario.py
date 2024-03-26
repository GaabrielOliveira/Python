class Funcionario:
    def __init__(self, nome:str, cargo:str, valor_hora_trabalhada:float):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

# Métodos de encapsulamento (get):
    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, valor):
        self.__horas_trabalhadas = valor

    @property
    def salario(self):
        return self.__salario

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1 #incremento de um

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada 

#-----------------------------------------------------------------------------------------
f1 = Funcionario(nome = "Fulano da Silva", cargo = "Programador", valor_hora_trabalhada = 35)

print("Salario", f1.salario) #funciona
print("Horas tranalhadas", f1.horas_trabalhadas) #funciona
f1.registra_hora_trabalhada()
f1.registra_hora_trabalhada()
f1.registra_hora_trabalhada()
f1.registra_hora_trabalhada()
f1.horas_trabalhadas = 12 #vai usar o setter
f1.calcula_salario()
print("Salario", f1.salario) #funciona
print("Horas tranalhadas", f1.horas_trabalhadas) #funciona
