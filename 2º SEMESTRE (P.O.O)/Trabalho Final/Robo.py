import random

class Robo:
    nivel_critico = 0.60

    def __init__(self, nome: str):
        self.nome = nome
        self._vida = round(random.uniform(0, 1), 2)

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > 1:
            self._vida = 1
        else:
            self._vida = valor

    def __repr__(self):
        return f'🤖 Nome do robô: {self.nome}, vida do robô: {self.vida} 🤖'

    def precisa_de_medico(self):
        return self.vida < Robo.nivel_critico


class RoboMedico(Robo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder_de_cura = random.uniform(0, 1)

    def curar(self, robo):
        if robo.vida < 1 and self.vida >= robo.vida:
            cura = min(1 - robo.vida, self.poder_de_cura)
            robo.vida += round(cura, 2)
            print(f'{self.nome} curou {robo.nome}. Nova vida: {robo.vida}')

    def atender_chamado(self):
        return random.choice([True, False])
