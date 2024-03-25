# N = 5
# nums = []
 
# for i in range(N):
#     num = (int(input(f"Informe o {i + 1} número: ")))
#     nums.append(num)
# print("Você digitou os seguintes números:")
# for i in range(N):
#     print(nums[i], end=" ")
    
    # 1ª nome da lista   2ªappend   3ªvariavel
    # append para add índices para a lista e adiciona um item naquele índice
    
    # ------------------------------------------------------------------------------
    
# qtd = 10
# nomes = ["maria", "ana", "francisca", "antonia", "adriana",\
#          "jose", "joao", "antonio", "francisco", "luiz"]
 
# print("Nomes:", nomes)
 
# print("\nAlterando...\n")

 
# for i in range(qtd):
#     nomes[i] = nomes[i].upper()
 
# print("Nomes alterados:", nomes)

    # ------------------------------------------------------------------------------

# Uma lista é como se fosse várias variáveis com o mesmo nome (o nome da lista).
# Você distingue entre as "variáveis" da lista (seus itens) com um índice numérico (posição do item na lista).
# O primeiro item da lista está no índice 0 e o restante conta a partir daí.
# Você acessa/modifica um item da lista pelo seu índice.
# Os índices da lista ficam dentro dos colchetes.
# Atenção: não coloque um índice maior do que o comprimento da lista para não dar erro!
# Diferentemente de arrays convencionais, que possuem um comprimento fixo definido na sua inicialização, listas em Python possuem comprimentos dinâmicos. Elas podem crescer ou diminuir seu comprimento conforme itens são adicionados ou excluídos.

    # ---------------------------------------------------------------------------------------------------------

# frutas = ["pequi", "pera", "pêssego", "pitanga", "pinha", "pitaia"]
# legumes = ["caxi", "cebola", "cenoura", "chuchu"]
 
# qtd_frutas = len(frutas)
# qtd_legumes = len(legumes)
 
# print("Eu tenho", qtd_frutas, "frutas e", qtd_legumes, "legumes.")

# ------------------------------------------------------------------------------------


#Desenvolvido por Prô Terra - MakerZine
#Para mais detalhes, acesse: https://www.makerzine.com.br

def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta == 0:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta = 0, temos um único valor de raiz (X1 = x2): ",x1)
  elif delta > 0:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta > 0, temos dois valores distintos de raízes: ",x1,"e",x2)
  else:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta < 0, não temos raízes reais!")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
bhaskara(a,b,c)