def funcao():
    print("eu imprimo essa mensagem apenas quando solicitado.")
 
 
def saudacoes(nome):
    print(f"Seja bem-vindo, {nome}!")
 
 
if __name__ == "__main__":
    print("eu imprimo essa mensagem somente quando executado diretamente")
    funcao()
    saudacoes("Pedro Siqueira")