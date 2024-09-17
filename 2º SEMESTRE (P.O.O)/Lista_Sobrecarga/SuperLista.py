class SuperLista():
    def _init_(self):
        self.__lista = [] # atributo de instância

    #sobrecarga do operador maior que >
    def _gt_(self, outro): 
        self.__lista.append(outro)
    
    def _repr_(self):
        if len(self.__lista) == 0:
            return "Lista vazia"
        else:
            return str(self.__lista)

# Testes

lis = SuperLista()
print(lis)
lis > 50
lis > 57
lis > 88
print(lis)