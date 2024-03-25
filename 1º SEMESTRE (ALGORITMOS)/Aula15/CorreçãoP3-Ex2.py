# Dados tres inteiros X,Y e Z, quais os inteiros múltiplos de Z entre X e Y inclusivos?  (FOR)

# FORMA A

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
z = int(input("Digite um número: "))

if x > y:
    aux = x
    x = y
    y = aux

for i in range(x, y +1):
    if i % z == 0:
        print(i)

# --------------------------------------------------------------------------

# FORMA B

x = int(input())
y = int(input())
z = int(input())

if x > y:
    aux = x
    x = y
    y = aux
if x % z != 0:
    x = x - x % z + z
for i in range (x, y +1, z):
    print(i)