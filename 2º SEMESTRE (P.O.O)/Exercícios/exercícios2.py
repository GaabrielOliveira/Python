
# EXERCÍCIO 1

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
# # getter
#     @property        
#     def age(self):
#         return self.__age

# # setter
#     @age.setter
#     def age(self, age):
#         self.__age = age


# stud = Student('Vanessa', 19)
# print('Name:', stud.name, stud.age) # obtém idade usando getter
# stud.age = 16 # altera idade usando setter
# print('Name:', stud.name, stud.age) # obtém idade usando getter

# #-----------------------------------------------------------------------------

# #EXERCÍCIO 2 - Bloqueie numero negativo


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
# # getter
#     @property        
#     def age(self):
#         return self.__age

# # setter
#     @age.setter
#     def age(self, age):
#         if age > 0:
#             self.__age = age

# stud = Student('Vanessa', 19)
# print('Name:', stud.name, stud.age) # obtém idade usando getter
# stud.age = 16 # altera idade usando setter
# print('Name:', stud.name, stud.age) # obtém idade usando getter

#-----------------------------------------------------------------------------

#EXERCICIO 3

class cadastro:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    #getters
    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha
    
    #setters
    @login.setter
    def login(self, login,):
        # if 5 >= len(login) <= 15:
            self.__login = login
        # else:
            # prin("O login deve conter entre 5 e 15 caracteres!")
        
    @senha.setter
    def senha(self, senha):
        # if len(senha) >= 8:
            self.__senha = senha
        # else:
            # print("A senha deve conter pelo menos 8 caracteres!")
        
        
logar = cadastro('gabfelipe2010@gmail.com', 'senha1')
print('Login:', logar.login, logar.senha)

logar.login = "gbafeliipe2010@gmail.com"
logar.senha = "senhasupersecreta1"

print('Login:', logar.login, logar.senha)    

# class cadastro:
#     def _init_(self, login, senha):
#         self.__login = None
#         self.__senha = None
#         self.login = login
#         self.senha = senha
    
#     # Getters
#     @property
#     def login(self):
#         return self.__login
    
#     @property
#     def senha(self):
#         return self.__senha
    
#     # Setters
#     @login.setter
#     def login(self, login):
#         if 5 <= len(login) <= 15:
#             self.__login = login
#         else:
#             print("O login deve conter entre 5 e 15 caracteres!")
        
#     @senha.setter
#     def senha(self, senha):
#         if len(senha) >= 8:
#             self.__senha = senha
#         else:
#             print("A senha deve conter pelo menos 8 caracteres!")
        
        
# logar = cadastro('gbafeliipe2010@gmail.com', 'senha1')
# print('Login:', logar.login, 'Senha:', logar.senha)

# logar.login = 'gbafeliipe2010@gmail.com'
# logar.senha = 'senhasupersecreta1'

# print('Login:', logar.login, 'Senha:', logar.senha)

#-----------------------------------------------------------------------------

#EXERCÍCIO 4

# class BombaCombustivel:
#     def __init__(self, valorLitro, quantidadeCombustivel):
#         self.valorLitro = valorLitro
#         self.quantidadeCombustivel = quantidadeCombustivel