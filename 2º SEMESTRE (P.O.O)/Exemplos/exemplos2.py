class ContaCorrente:
    def __init__(self, numero : int, saldo: float):
        self.numero = numero
        self.__saldo = saldo                                    #ao colocar __ ele se trona privado

    def getSaldo(self):                                         #método getter (para visalizar o saldo)
        return self.__saldo
    
    def setSaldo(self, valor : float):                           #método setter
        self.__saldo = valor

    def depositar(self, valor : float):
        if valor > 0:
            self.__saldo = self.__saldo + valor
        else:
            print("O valor deve ser maior que zero!")

    def sacar(self, valor : float):
        if self.__saldo >= valor:
            self.__saldo = self.__saldo - valor
        else:
            print("Saldo insuficiente!")

# --------------------------
c1 = ContaCorrente(123456, 1000)
c2 = ContaCorrente(654321, 500)

print(f"ContaCorrente nº:{c1.numero}, R$ {c1.getsaldo()}")
c1.saldo = 1000000      
c1.setSaldo(100000000)                                        #não vai funcionar
print(f"ContaCorrente nº:{c1.numero}, R$ {c1.getsaldo()}")
# c1.depositar(900)
# print(f"Novo saldo: R$ {c1.saldo}")
# c1.sacar(2000)
# print(f"Novo saldo: R$ {c1.saldo}")