# # # # print("\nversão 1")
# # # # i = 10
# # # # if i < 20:
# # # #     print(i, end=" ")
# # # #     i = i + 1
# # # # print(i)

# -------------------------

# # # # print("\nversão 2")
# # # # i = 10
# # # # while i < 20:
# # # #     print(i, end=" ")
# # # #     i = i + 1
# # # # print(i)

# -------------------------

# # # # print("\nversão 3")
# # # # i = 100
# # # # if i < 20:
# # # #     print(i, end=" ")
# # # #     i = i + 1
# # # # print(i)

# -------------------------

# # # # print("\nversão 4")
# # # # i = 100
# # # # while i < 20:
# # # #     print(i, end=" ")
# # # #     i = i + 1
# # # # print(i)

# -------------------------

# # # # print("\nversão 5")
# # # # i = 1
# # # # if i < 20:
# # # #     print(i, end=" ")
# # # # print(i)

# -------------------------

# # # # print("\nversão 6")
# # # # i = 1
# # # # while i < 20:
# # # #     print(i, end=" ")
# # # # print(i)

# -------------------------

# # # print("\nversão 2")
# # # i = 10
# # # while i < 20:
# # #     print(i, end=" ")
# # #     i = i + 1
# # # print(i)

# ------------------------

# # total = 0
# # contador = 1

# # # Use um loop para ler as notas dos cinco estudantes
# # while contador <= 5:
# #     nota = float(input(f"Digite a nota do {contador}º estudante (entre 0 e 10): "))
# #     total = total + nota
# #     contador = contador + 1
 
# # # Calcule a média
# # media = total / 5
 
# # # Escreve a média da classe
# # print("A média da classe é:", media)

# -------------------------------------

# total = 0
# contador = 0
# nota = float(input("Digite a nota do estudante (ou -1 para encerrar): "))
 
# while nota != -1:
#     if 0 <= nota <= 10:
#         total = total + nota
#         contador = contador + 1
#     else:
#         print("A nota deve estar entre 0 e 10. Tente novamente.")
 
#     nota = float(input("Digite a nota do estudante (ou -1 para encerrar): "))
 
# if contador > 0:
#     media = total / contador
#     print("A média da classe é:", media)
# else:
#     print("Nenhuma nota válida foi inserida.")]

# ------------------------------------------------

# EXERCÍCIOS:
# 1-

# Inicialize as variáveis para contar os aprovados e reprovados
aprovados = 0
reprovados = 0
 
# Inicialize a variável para contar o número de estudantes
contador = 0
 
# Use um loop while para ler os resultados de cada estudante
while contador < 10:
    nome = input("Digite o nome do estudante: ")
    resultado = input("Digite o resultado do estudante (True para aprovado, False para reprovado): ").lower() == 'true'
 
    # Verifique o resultado e atualize as contagens
    if resultado:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
 
    contador = contador + 1
 
# Escreve a quantidade de estudantes aprovados e reprovados
print("Quantidade de estudantes aprovados:", aprovados)
print("Quantidade de estudantes reprovados:", reprovados)
 
# Verifique se mais de oito estudantes foram aprovados
if aprovados > 8:
    print("Bônus ao instrutor!")

