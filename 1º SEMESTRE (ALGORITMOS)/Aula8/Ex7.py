# Dados três números, qual o maior?

x = float(input("Digite um numero: "))
y = float(input("Digite um numero: "))
z = float(input("Digite um numero: "))
 
maior = 0

if x > y:
    if x > z:
        maior = x
    else:
        maior = z
else:
    if y > z:
        maior = y
    else:
        maior = z
 
print("o maior número é", maior)
