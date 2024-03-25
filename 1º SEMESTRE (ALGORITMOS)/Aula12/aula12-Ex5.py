# Dados dois números, um deles é múltiplo do outro?

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))

if x % y == 0 or y % x == 0:
    print("SIM")
else:
    print("NÃO")