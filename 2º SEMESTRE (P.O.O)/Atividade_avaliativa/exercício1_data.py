# Exercício 1
# Crie uma classe para representar datas.
# a) Represente uma data usando três atributos: o dia, o mês, e o ano.
# b) Sua classe deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos.
# c) Forneça um método set um get para cada atributo.
# d) Forneça o método __str__ para retornar uma representação da data como string. Considere que a data deve ser formatada mostrando o dia, o mês e o ano separados por barra (/).
# e) Forneça uma operação para avançar a data para o dia seguinte.
# f) Escreva código de teste que instancie objetos de exemplo e demonstre as capacidades da classe.
# Garanta que uma instância desta classe sempre esteja em um estado consistente.

dia_por_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
class Data:
    def __init__(self, dia : int, mes : int, ano : int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        if not self.__validar_data:
            print("Insira uma data válida!🤬")
            return None

    # def __validar_data(self):
    #     if self.mes < 1 or self.mes > 12:
    #         print(f"nem tem esse mes {self.mes} press tenção minino")
    #         return False
    #     else:
    #         return True
            
    #     if self.dia < 1 or self.dia > dia_por_mes[self.__mes]:
    #         print(f"o dia {self.dia} é invalido para o mes {self.mes}! coloca um dia valido mizera")
    #         return False
    #     else:
    #         return True
    
    def __validar_data(self):
        mes_invalido = self.__mes < 1 or self.__mes > 12
        dia_invalido = mes_invalido or self.__dia < 1 or self.__dia > dia_por_mes[self.__mes]
        return bool(not dia_invalido and not mes_invalido)
         
    def prox_dia(self):
        if not self.__validar_data():
            return "Insira uma data válida!🤬"
        
        ultimo_dia = dia_por_mes[self.__mes] == self.__dia
        ultimo_mes = self.__mes == 12
        dia = self.__dia
        mes = self.__mes
        ano = self.__ano
        
        if ultimo_dia:
            dia = 1
            mes += 1
            
        if ultimo_mes:
            mes = 1
            ano += 1
            
        if not ultimo_dia and not ultimo_mes:
            dia += 1
            
        return f'{dia:02}/{mes:02}/{ano:02}'

    @property
    def dia(self):
        return self.__dia
         
    @property
    def mes(self):
        return self.__mes
        
    @property
    def ano(self):
        return self.__ano
    
    @dia.setter
    def dia(self, dia : int):
        self.__dia = dia
            
    @mes.setter
    def mes(self, mes : int):
        self.__mes = mes
            
    @ano.setter
    def ano(self, ano : int):
        self.__ano = ano
            
    def __str__(self):
        if not self.__validar_data:
            return "Insira uma data válida!🤬"
        return f'{self.dia:02}/{self.mes:02}/{self.ano:02}'
# --------------------------------------------------------------------
data = Data(31, 3, 2022 )
print("\nData atual:", data,"\nProxima data:", data.prox_dia())

data = Data(29, 2, 2022 )
print("\nData atual:", data,"\nProxima data:", data.prox_dia())



