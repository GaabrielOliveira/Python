from Robo import Robo
from RoboLutador import RoboLutador
from RoboMedico import RoboMedico

# Método para inicar a luta
def lutar_ate_o_fim(robo1, robo2, medico):
    print(f'Iniciando a luta entre {robo1.nome} e {robo2.nome}!')
    
    while robo1.vida > 0 and robo2.vida > 0:
        input(f'🎮 Pressione Enter para continuar...🎮\n')  # Pausa até o usuário apertar Enter
        robo1.atacar(robo2)
        
        if robo2.vida < 0.1:
            input("🚑 Pressione Enter para chamar o médico...🚑")  # Pausa para o médico ser chamado
            if medico.atender_chamado():
                print(f'🤩 {medico.nome} atendeu ao chamado!🤩')
                medico.curar(robo2)
            else:
                print(f'💀 {medico.nome} não atendeu ao chamado.💀')

        if robo2.vida > 0:
            input(f'Pressione Enter para continuar...\n')  # Pausa até o usuário apertar Enter
            robo2.atacar(robo1)

            if robo1.vida < 0.1:
                input("🚑 Pressione Enter para chamar o médico...🚑")  # Pausa para o médico ser chamado
                if medico.atender_chamado():
                    print(f'🤩 {medico.nome} atendeu ao chamado!🤩')
                    medico.curar(robo1)
                else:
                    print(f'💀 {medico.nome} não atendeu ao chamado.💀')

    if robo1.vida > 0:
        print(f'🎉 {robo1.nome} é o vencedor da luta!🎉')
    elif robo2.vida > 0:
        print(f'🎉 {robo2.nome} é o vencedor da luta!🎉')
    else:
        print('🤷‍♂️ A luta terminou em empate, ambos foram derrotados!🤷‍♂️')

# Definido o nome de cada robo (Inspirado em Overwatch)
roboL1 = RoboLutador("Reinhardt")
roboL2 = RoboLutador("Bastion")
medico = RoboMedico("Zenyatta")


print(f'Vida inicial de {roboL1.nome}: {roboL1.vida}')
print(f'Vida inicial de {roboL2.nome}: {roboL2.vida}')
# Participantes da luta
lutar_ate_o_fim(roboL1, roboL2, medico)


