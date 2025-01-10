Entrada = int(input())

print("Lumberjacks:")

for _ in range(Entrada):
    numeros = list(map(int, input().split()))

    if numeros == sorted(numeros) or numeros == sorted(numeros, reverse=True):
        print("Ordered")
    else:
        print("Unordered")