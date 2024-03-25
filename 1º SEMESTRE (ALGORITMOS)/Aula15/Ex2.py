# Dada uma sequência de inteiros, que termina com 10 números ou com um múltiplo de 6. Qual a soma dos múltiplos de 3 e a soma dos múltiplos de 2? O múltiplo de 6 deve ser contabilizado na soma. Utilize break.

soma = 0
print('digite 10 números...')
for i in range (0 , 10):
    n = int(input())
    if n % 6 == 0:
        break
    if n % 3 == 0:
        soma += n
print("a soma dos múltiplos de 3 é" , soma)