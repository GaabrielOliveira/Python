# class ContaCorrente :
#     def __init__(self, numero, saldo)
#         self.numero = numero
#         self.saldo = saldo
#     def depositar(self, )


class ContaCorrente:
    def __init__(self, numero : int, saldo: float):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor : float):
        if valor > 0:
            self.saldo = self.saldo + valor
        else:
            print("O valor deve ser maior que zero!")

    def sacar(self, valor : float):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente!")

# --------------------------
c1 = ContaCorrente(123456, 1000)
c2 = ContaCorrente(654321, 500)

print(f"ContaCorrente nº:{c1.numero}, R$ {c1.saldo}")
c1.saldo = 1000000
c1.depositar(1000000) 
print(f"ContaCorrente nº:{c1.numero}, R$ {c1.saldo}")
# c1.depositar(900)
# print(f"Novo saldo: R$ {c1.saldo}")
# c1.sacar(2000)
# print(f"Novo saldo: R$ {c1.saldo}")
