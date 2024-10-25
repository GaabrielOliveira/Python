def max_filas_linear(n):
    guerreiros = 0
    filas = 0
    while guerreiros + filas + 1 <= n:
        filas += 1
        guerreiros += filas
    return filas


testes = int(input("Indique a quantidade de casos de teste: "))
for _ in range(testes):
    n = int(input("Indique a quantidade de guerreiros: "))
    print(max_filas_linear(n))
