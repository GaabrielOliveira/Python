import random
from Robo import Robo

class RoboMedico(Robo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder_de_cura = random.uniform(0, 1)

    def curar(self, robo):
        if robo.vida < 1 and self.vida >= robo.vida:
            cura = min(1 - robo.vida, self.poder_de_cura)
            robo.vida += round(cura, 2)
            print(f'👌 {self.nome} curou {robo.nome}👌! Nova vida: {robo.vida}')

    def atender_chamado(self):
        return random.choice([True, False])
     