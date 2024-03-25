# Um natural é dito triangular se ele é produto de três naturais consecutivos. Exemplo: 120 é triangular, pois 4⋅5⋅6=120. Dado um natural, ele é triangular?

num = int(input("digite um numero natural:" ))
n = 1
triangular =  n * (n+1) * (n+2)

while triangular < num:
    n += 1
    triangular = n * (n+1) * (n+2)
    
if triangular == num:
    print(f' {num} é triangular')
    print(f" {n} * {n+1} * {n+2} = {num}")
else:
    print(f' {triangular} NÃO é triangular)')