# Dados três números, todos são múltiplos de 5 ou de 3?

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))
z = int(input("Digite um numero: "))

if (x % 5 == 0 or x % 3 == 0) and (y % 5 == 0 or y % 3 == 0) and (z % 5 == 0 or z % 3 == 0):
    print("SIM")
else:
    print("NÃO")