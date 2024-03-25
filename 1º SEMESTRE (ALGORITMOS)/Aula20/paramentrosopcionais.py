# def construir_nome(primeiro_nome, ultimo_nome, nome_do_meio="", prefixo="", sufixo=""):
    
#     nome_completo = ""
 
#     if prefixo != "":
#         nome_completo = f"{prefixo} "
 
#     nome_completo += f"{primeiro_nome}"
 
#     if nome_do_meio != "":
#         nome_completo += f" {nome_do_meio}"
 
#     nome_completo += f" {ultimo_nome}"
 
#     if sufixo != "":
#         nome_completo += f" {sufixo}"
 
#     return nome_completo
 
 
# print(construir_nome("Maria", "da Silva"))
# print(construir_nome("José", "Ferreira", "dos Santos"))
# print(construir_nome("Pedro", "de Bragança", sufixo="II", prefixo="Dom"))

def multiplicar_por_dois(numero):
    return numero * 2
 
s = "2.7"
f = float(s)
i = int(f)
# i = int(a) # essa conversão daria erro
 
print(multiplicar_por_dois(s))
print(multiplicar_por_dois(f))
print(multiplicar_por_dois(i))
