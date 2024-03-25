# Dados três números, todos são múltiplos de 10?

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))
z = int(input("Digite um numero: "))

if x % 10 == 0 and y % 10 == 0 and z % 10 == 0:
    print("SIM")
else:
    print("NÃO")