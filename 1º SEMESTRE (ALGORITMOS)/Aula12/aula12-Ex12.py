# Dados três números representando os lados de um triângulo, ele é equilátero, isósceles ou escaleno?

x = float(input("Digite um numero: "))
y = float(input("Digite um numero: "))
z = float(input("Digite um numero: "))

if (x == y == z) or (x == y != z ) or (x != y != z):
    if (x == y == z):
        print ("Equilatero")
    if (x == y != z):
        print ("Isósceles")
    if (x != y != z):
        print ("Escaleno")
