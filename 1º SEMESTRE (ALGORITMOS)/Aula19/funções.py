# # # def menu():
# # #     print("Escolha uma opção...")
# # #     print("1) Criar")
# # #     print("2) Buscar")
# # #     print("3) Editar")
# # #     print("4) Remover")
# # #     print("0) Sair")
 
 
# # # if __name__ == "__main__":
# # #     while True:
# # #         menu()
# # #         user_input = int(input())
# # #         if user_input == 0:
# # #             break
# # #         else:
# # #             print("Opção ainda não implementada!")

# # import random
 
# # def random_between_1_and_10():
# #     d = random.random() * 10
# #     i = int(d) + 1
# #     return i
 
# # if __name__ == "__main__":
# #     print("Gerando 100 números aleatórios entre 1 e 10:")
# #     v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# #     for i in range(100):
# #         v[random_between_1_and_10()] += 1
 
# #     for i in range(1, len(v)):
# #         if v[i] > 0:
# #             print(f"Número {i} gerado {v[i]} vezes.")

# def upper_case_substring(s, i, j):
#     """torna maiúsculas as letras entre os índices i e j da string s"""
#     before = s[:i]
#     uppercase = s[i:j].upper()
#     after = s[j:]
#     return before + uppercase + after
 
# if __name__ == "__main__":
#     frase = "cada minuto que passa é outra chance de mudar tudo"
#     print(upper_case_substring(frase, 30, 36))
 
#     # erro! nenhum argumento bate com os parâmetros!
#     # print(upper_case_substring(True, frase))

