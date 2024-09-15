import random
from Robo import Robo

class RoboLutador(Robo):
    dano_maximo = 0.2

    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder = random.uniform(RoboLutador.dano_maximo, 1)

    def atacar(self, robo_oponente):
        if robo_oponente.vida <= 0:
            print(f'{robo_oponente.nome} já foi derrotado!')
            return

        dano = round(robo_oponente.vida * (1 - self.poder), 2)
        robo_oponente.vida -= dano
        robo_oponente.vida = round(robo_oponente.vida, 2)
        print(f'😮 {self.nome} deu {dano} de dano em {robo_oponente.nome}😮. Vida do oponente: {robo_oponente.vida}➕')

        if robo_oponente.vida <= 0:
            print(f'😮 {robo_oponente.nome} foi derrotado!😮 {self.nome} é o vencedor!🎉')
            return

        # Se o oponente for um RoboLutador, ele contra-ataca
        if isinstance(robo_oponente, RoboLutador):
            robo_oponente.contra_atacar(self)

    def contra_atacar(self, robo_oponente):
        if self.vida <= 0:
            print(f'👎 {self.nome} já foi derrotado e não pode contra-atacar!👎')
            return

        dano = round(self.vida * (1 - robo_oponente.poder), 2)
        robo_oponente.vida -= dano
        robo_oponente.vida = round(robo_oponente.vida, 2)
        print(f'{self.nome} contra-atacou {robo_oponente.nome} com {dano} de dano!💥 Vida do oponente: {robo_oponente.vida}➕')

        if robo_oponente.vida <= 0:
            print(f'{robo_oponente.nome} foi derrotado!😮 {self.nome} é o vencedor!🎉')