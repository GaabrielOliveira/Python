# O fatorial de um número é o produto dele pelos seus antecessores maiores que 0. Dado um natural, qual seu fatorial?

n = int(input("Digite um número: "))
f = 1
for i in range(1, n +1):
    f *= i
print(f)