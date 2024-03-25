# ord -> transformar um caractere em codigo
# chr -> transformar um codigo em um caractere


# EXEMPLOS AULA 9


# 1-

# print("um texto\0outro texto")
# print("um texto\aoutro texto")
# print("um texto\boutro texto")
# print("um texto\toutro texto")
# print("um texto\noutro texto")
# print("um texto\voutro texto")
# print("um texto\foutro texto")
# print("um texto\routro texto")


# 2-

# a = 97
# U = 85
# cifrao = 36
# maior = ">"
# arroba = "@"
# dois = "2"
 
# print(a, chr(a))
# print(U, chr(U))
# print(cifrao, chr(cifrao))
# print(maior, ord(maior))
# print(arroba, ord(arroba))
# print(dois, ord(dois))


# 3-

# c1 = "d"
# c2 = "h"
# n1 = 7
 
# c3 = chr(n1 + ord(c1))
# print(n1, "letras depois de", c1, "é", c3)
 
# n2 = ord(c2) - ord(c1) - 1
# print("há", n2, "letras entre", c1, "e", c2)
 
# c4 = ord(c1) * ord(c2)
# print(c1, "*", c2, "=", c4)
 
# n3 = ord(c1) + ord(c2)
# print(c1, "+", c2, "=", n3)


# (Segunda parte da aula).
# 4- Alatoriedade

# import random
 
# sorteia um float no intervalo [0,1)
# sorteado = random.random()
# print(sorteado)
 
# # transforma em um float entre [0,10)
# sorteado = sorteado * 10
# print(sorteado)
 
# # descarta a parte decimal
# int_sorteado = int(sorteado)
# print(int_sorteado)


# 5-

# import random
# n = 20
# sorteado = int(random.random()*n)
# print(sorteado)


# 6-

# primeiro = 10
# ultimo = 20
# quantidade = ultimo - primeiro + 1
# sorteado = primeiro + int(random.random() * quantidade)


# 7-

# primeiro = 50
# ultimo = 100
# diferenca = 5
# quantidade = (ultimo - primeiro) / diferenca + 1
# sorteado = primeiro + diferenca * int(random.random() * quantidade)


# Sementes:

# 8-

# import random
        
# random.seed(2)
 
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())

