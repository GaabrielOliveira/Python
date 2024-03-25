# Dados três números representando os lados de um triângulo, ele é equilátero, isósceles ou escaleno? (como seria esse exercício sem o else?)

# n1 = float(input("Digite um numero: "))
# n2 = float(input("Digite um numero: "))
# n3 = float(input("Digite um numero: "))

# if n1 == n2 == n3:
#     print("É um triangulo equilatero")
    
# if n1 == n2 != n3:
#     print("É um triangulo Isóceles")
    
# if n1 != n2 != n3:
#     print("É um triangulo Escaleno")
    
    
#     # Dados três números representando os lados de um triângulo, ele é equilátero, isósceles ou escaleno? (como seria esse exercício sem o else?)

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
n3 = float(input("Digite um numero: "))

if n1 == n2 == n3:
    print("É um triangulo equilatero")
else:
    print("Não é um triangulo equilatero")
    
if n1 == n2 != n3:
    print("É um triangulo Isóceles")
else:
    print("Não é um triangulo Isóceles")
    
if n1 != n2 != n3:
    print("É um triangulo Escaleno")
else:
    print("Não é um triangulo Escaleno")