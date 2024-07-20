# Exercício 2

def juntar_dicionarios(dict1, dict2):
    dict_junto = {}

    for chave, valor in dict1.items():
        dict_junto[chave] = valor
    
    for chave, valor in dict2.items():
        dict_junto[chave] = valor

    return dict_junto

# Teste
dict1 = {'Um': 1, 'Dois': 2, 'Três': 3}
dict2 = {'Quatro': 4, 'Cinco': 5, 'Seis': 6}
dict_junto = juntar_dicionarios(dict1, dict2)
print(dict_junto)

