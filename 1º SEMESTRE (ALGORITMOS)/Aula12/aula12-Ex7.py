# Dados dois números, algum deles NÃO é múltiplo de 5?

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))

if x % 5 != 0 or y % 5 != 0:
    print("SIM")
else:
    print("NÃO")