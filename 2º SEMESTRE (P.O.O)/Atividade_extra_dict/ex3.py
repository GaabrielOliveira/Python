# Exercício 3

def extract(dicionario, chave):
    novo_dicionario = {}
    for chave in chaves:
        if chave in dicionario:
            novo_dicionario[chave] = dicionario[chave]
    return novo_dicionario

# Teste
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'd': 5, 'e': 6}
chaves = ['a', 'c', 'e']
novo_dicionario = extract(dicionario, chaves)
print(novo_dicionario)