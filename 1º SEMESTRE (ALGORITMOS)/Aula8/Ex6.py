# Dados dois números, qual o maior deles e a diferença absoluta entre eles? (a diferença absoluta é o maior menos o menor).

N1 = int(input("N1: "))
N2 = int(input("N2: "))

if N1 < N2 :
    print("maior = N2")
else:
    print("maior = N1")
     
diferença = N1 - N2

print(" A diferença absoluta é", diferença)


