# Dado um inteiro, quantos digitos ele tem?

n = int(input("Digite um número: "))
cont = 0
while n != 0:
    n//= 10
    cont += 1
print(cont)