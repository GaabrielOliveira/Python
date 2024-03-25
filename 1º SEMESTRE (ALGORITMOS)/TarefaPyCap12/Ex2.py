# Ex-2: Dada uma sequência de inteiros, que termina com 10 números ou com um múltiplo de 6. Qual a soma dos múltiplos de 3? O múltiplo de 6 não deve ser contabilizado na soma.

soma_multiplos_de_3 = 0
soma_multiplos_de_2 = 0

multiplo_de_6_inserido = False

contador = 0
while contador < 10 and not multiplo_de_6_inserido:
    numero= int(input("Digite uma sequência de 10 números inteiros (ou 1 multiplo de 6 para encerrar): "))
    contador += 1
    
    if numero % 6 == 0:
        multiplo_de_6_inserido = True
    if numero % 3 == 0:
        soma_multiplos_de_3 += numero
    if numero % 2 == 0:
        soma_multiplos_de_2 += numero
        
print(f"A soma dos múltiplos de 3 é: {soma_multiplos_de_3}")
print(f"A soma dos múltiplos de 2 é: {soma_multiplos_de_2}")