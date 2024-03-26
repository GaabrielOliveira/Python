class Cadastro:
    def _init_(self, login, senha):
        self.login = login
        self.senha = senha
    
    # Getters
    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha
    
    # Setters
    @login.setter
    def login(self, login):
        if len(login) >=5 and len(login) <= 15:
            self.__login = login
        else:
            print("O login deve conter entre 5 e 15 caracteres!")
        
    @senha.setter
    def senha(self, senha):
        if len(senha) >= 8:
            self.__senha = senha
        else:
            print("A senha deve conter pelo menos 8 caracteres!")
        
        
cadastro = Cadastro('gbafeliipe2010@gmail.com', 'senha1')
print('Login:', cadastro.login, 'Senha:', cadastro.senha)

cadastro.login = 'gbafeliipe2010@gmail.com'
cadastro.senha = 'senhasupersecreta1'

print('Login:', cadastro.login, 'Senha:', cadastro.senha)
        
# logar = Cadastro('gbafeliipe2010@gmail.com', 'senha1')
# print('Login:', logar.login, 'Senha:', logar.senha)

# logar.login = 'gbafeliipe2010@gmail.com'
# logar.senha = 'senhasupersecreta1'

# print('Login:', logar.login, 'Senha:', logar.senha)