# Exercício 1

def dicionario_list(lista_chave, lista_valor):
    if len(lista_chave) != len(lista_valor):
        return "Erro: As listas devem ter o mesmo tamanho!"
    
    dicionario = {}
    for i in range(len(lista_chave)):
        dicionario[lista_chave[i]] = lista_valor[i]
    
    return dicionario

# Testes
lista_chave = ['Um', 'Dois', 'Três', 'Quatro', 'Cinco']
lista_valor = [1, 2, 3, 4, 5]
dicionario = dicionario_list(lista_chave, lista_valor)
print(dicionario)

# Teste de erro
lista_chave = ['Um', 'Dois', 'Três', 'Quatro', 'Cinco']
lista_valor = [1, 2, 3]
dicionario = dicionario_list(lista_chave, lista_valor)
print(dicionario)
