# Dados tres inteiros X,Y e Z, quais os inteiros múltiplos de Z entre X e Y inclusivos? (WHILE)

# FORMA A

# x = int(input("Digite um número: "))
# y = int(input("Digite um número: "))
# z = int(input("Digite um número: "))

# if x > y:
#     aux = x
#     x = 4
#     y =  aux
# while x <= y:
#     if x % z == 0:
#         print(x)
#     x += 1
    
# -----------------------------------------------------------------------------------------------

# FORMA B

# x = int(input("Digite um número: "))
# y = int(input("Digite um número: "))
# z = int(input("Digite um número: "))

# if x > y:
#     aux = x
#     x = 4
#     y =  aux
# while x <= y:
#     print(x)
#     x += z

# -----------------------------------------------------------------------------------------------

# FORMA C

# x = int(input("Digite um número: "))
# y = int(input("Digite um número: "))
# z = int(input("Digite um número: "))

# if x > y:
#     aux = x
#     x = 4
#     y =  aux
# if x % z != 0:
#     x = x - x % z + z
# while x <= y:
#     print(x)
    
    
