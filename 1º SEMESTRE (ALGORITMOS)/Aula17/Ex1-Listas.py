# EXERCÍCIO 1: Ler uma lista de n itens. Escrever os n itens normalmente em uma linha e do último para o primeiro em outra linha.

n = int(input("Quantidade de itens: "))
lista = []

print("Digite os {n} itens:")
for i in range(n):
    numero = input()
    lista.append(numero)

print("imprimindo normalmente...")
print(lista)

print("Imprimindo de trás para frente")
for i in range(n - 1, -1, -1):
    print(lista[i], end=" ")