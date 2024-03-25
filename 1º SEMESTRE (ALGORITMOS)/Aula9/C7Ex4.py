# Exercicio 4 (Lista nª 07)
# Dada uma letra, ela é maiúscula ou minúscula?

letra = input("digite uma letra: ")
codigo = ord(letra)
if 65 <= codigo <= 90:
    print('letra Maiúscula')
elif 97 <= codigo <= 122:
    print('Letra Minúscula')
else:
    print('Colabora né')
