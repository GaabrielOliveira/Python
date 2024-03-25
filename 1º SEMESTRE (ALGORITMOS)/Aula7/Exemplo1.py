print("Boletim Digital")
print("###############\n")
 
t = float(input("Trabalho: "))
s = float(input("Seminário: "))
p = float(input("Prova: "))
m = (t * 2 + s * 3 + p * 5) / 10
 
print("\nMédia:", m)
if m >= 8.5:
    print("Conceito A, aprovado :D")
elif m >= 7:
    print("Conceito B, aprovado :)")
elif m >= 5:
    print("Conceito C, recuperação :|")
elif m >= 2.5:
    print("Conceito D, recuperação :(")
else:
    print("Conceito E, reprovado :O")
