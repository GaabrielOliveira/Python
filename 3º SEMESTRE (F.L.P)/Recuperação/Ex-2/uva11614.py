import math

def max_filas(n):
    k = int((math.sqrt(1 + 8 * n) - 1) // 2)
    return k

testes = int(input("Informe a quantidade de testes: "))
for _ in range(testes):
    n = int(input())
    print(max_filas(n))