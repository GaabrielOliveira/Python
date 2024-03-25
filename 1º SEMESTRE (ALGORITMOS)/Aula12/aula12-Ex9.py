# Dados três números, nenhum deles é múltiplo de 5 e de 3?

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))
z = int(input("Digite um numero: "))

if (x % 5 == 0 or x % 3 == 0) and (y % 5 == 0 or y % 3 == 0) and (z % 5 == 0 or z % 3 == 0):
    print("NÃO")
else:
    print("SIM")