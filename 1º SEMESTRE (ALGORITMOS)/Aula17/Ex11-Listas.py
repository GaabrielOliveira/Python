#EXERCÍCIO 11: Ler um natural n, indicando a capacidade máxima de itens em uma lista, seguido por uma série de duplas i e �x. Cada dupla representa um índice �i e seu respectivo item �x na lista. Encerrar a leitura ao encontrar um índice inválido. Caso não seja fornecido um determinado índice, considerar seu item como zero. Escrever a lista resultante.

n = int(input("Digite o tamanho da lista: "))
lista = []
for i in range(n):
    lista.append(0)

while True:
    i = int(input("Digite um índice: "))
    if i >= n or i< 0:
        print("Índice invalido! encerrando a leitura...")
        break
    x = int(input("Digite um item: "))
    
    lista[i] = x

print("Alista resultante é: ")
print(lista)
    