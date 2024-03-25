# Dado um numero , qual o seu fatorial?

num = int(input())
resultado = 1

for n in range (1, num + 1):
    resultado *= n
print(resultado) 