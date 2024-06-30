# Dado um inteiro, qual o seu reverso? Exemplo de entrada→saída: 5837→7385.
# Exercício 10

orig = int(input('Digite um numero inteiro: '))
inv = 0
while orig != 0:
    resto = orig % 10
    inv = inv * 10 + resto
    orig = orig // 10
print(inv)


# Exercício 14

# Dado um natural, qual seu fatorial?
#  n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(resultado)

