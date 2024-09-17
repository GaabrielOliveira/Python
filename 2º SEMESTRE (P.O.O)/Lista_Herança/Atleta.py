class Atleta:
    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        self.aposentado = True
        print("Atleta aposentado.")

    def aquecer(self):
        print("Atleta se aquecendo.")

class Corredor(Atleta):
    def correr(self):
        print("Corredor está correndo.")

class Nadador(Atleta):
    def nadar(self):
        print("Nadador está nadando.")

class Ciclista(Atleta):
    def pedalar(self):
        print("Ciclista está pedalando.")

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)


tri_atleta = TriAtleta(False, 75)
tri_atleta.aquecer()
tri_atleta.correr()
tri_atleta.nadar()
tri_atleta.pedalar()