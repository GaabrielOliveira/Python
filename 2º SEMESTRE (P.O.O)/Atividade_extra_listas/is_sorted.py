# Exercício 5

def is_sorted(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

primeira_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
segunda_lista = [3, 2, 5, 6, 1, 6, 10]

print(is_sorted(primeira_lista))
print(is_sorted(segunda_lista))