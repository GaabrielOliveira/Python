import sys

for line in sys.stdin:
    data = list(map(int, line.split()))
    n = data[0]
    sequencia = data[1:]
    
    if n == 1:
        print("Jolly")
        continue
    
    diferencas = set(abs(sequencia[i] - sequencia[i - 1]) for i in range(1, n))
    diferencas_esperadas = set(range(1, n))
    
    if diferencas == diferencas_esperadas:
        print("Jolly")
    else:
        print("Not jolly")