def cumsum(lista):
    resultado = []
    soma = 0

    for numero in lista:
        soma += numero
        resultado.append(soma)
    
    return resultado

lista_numeros = [1, 5, 10, 15, 20]
print(cumsum(lista_numeros))