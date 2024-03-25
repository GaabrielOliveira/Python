# Dado um número, ele é múltiplo de 3 ou 5, mas não simultaneamente pelos dois?

x = int(input("Digite um numero: "))

if x % 3 == 0 and x % 5 == 0:
    print("NÃO")
elif x % 3 != 0 and x % 5 != 0:
    print("NÃO")
else:
    print("SIM")