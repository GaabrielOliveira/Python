# Exercício 4

def chop(lista):
    if len(lista) > 2:
        lista[0] = lista[1]
        lista.pop()
        lista.pop(0)
    elif len(lista) == 2:
        lista.pop()
        lista.pop(0)

list = [4, 8, 5, 7]
chop(list)
print(list)