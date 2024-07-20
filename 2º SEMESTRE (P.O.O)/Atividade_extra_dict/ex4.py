# Exercício 4

def criar_dicionario_quadrado(k):
    if k < 1:
        return "Erro: O valor de 'k' deve ser um inteiro positivo ou >= 1"

    dicionario_quadrado = {i: i**2 for i in range(1, k + 1)}
    return dicionario_quadrado

# Teste
k = 5
dicionario_teste = criar_dicionario_quadrado(k)
print(dicionario_teste)

# Teste de erro
k_erro = -5
dicionario_teste_erro = criar_dicionario_quadrado(k_erro)
print(dicionario_teste_erro)