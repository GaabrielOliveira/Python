# Dada uma sequência de 10 inteiros, qual a soma dos múltiplos de 3 e a soma dos múltiplos de 2? Entretanto, múltiplos de 6 não devem ser contabilizados na soma. Utilize continue.

soma = 0
print('digite 10 números...')
for i in range (0 , 10):
    n = int(input())
    if n % 6 == 0:
        continue
    if n % 3 == 0:
        soma += n
print("a soma dos múltiplos de 3 é" , soma)