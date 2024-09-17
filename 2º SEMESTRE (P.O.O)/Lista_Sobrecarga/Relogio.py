class Relogio:
    def __init__(self, hr=0, min=0, segs=0):
        if not (0 <= hr < 24):
            print("Horário digitado inválido")
            self.hr = 0
        else:
            self.hr = hr

        if not (0 <= min < 60):
            print("Minuto digitado inválido")
            self.min = 0
        else:
            self.min = min

        if not (0 <= segs < 60):
            print("Segundo digitado inválido")
            self.segs = 0
        else:
            self.segs = segs

    def __repr__(self):
        return f"{self.hr:02}:{self.min:02}:{self.segs:02}"

    def __add__(self, outro):
        segs = self.segs + outro.segs
        min = self.min + outro.min + segs // 60
        hr = self.hr + outro.hr + min // 60

        return Relogio(hr % 24, min % 60, segs % 60)

    def __sub__(self, outro):
        total_segs_1 = self.hr * 3600 + self.min * 60 + self.segs
        total_segs_2 = outro.hr * 3600 + outro.min * 60 + outro.segs

        if total_segs_1 < total_segs_2:
            print("O primeiro horário deve ser maior que o segundo")
            return None

        diferenca_segs = total_segs_1 - total_segs_2
        hr = diferenca_segs // 3600
        min = (diferenca_segs % 3600) // 60
        segs = diferenca_segs % 60

        return Relogio(hr, min, segs)

    def __eq__(self, outro):
        return (self.hr == outro.hr and
                self.min == outro.min and
                self.segs == outro.segs)

    def __gt__(self, outro):
        return (self.hr, self.min, self.segs) > (outro.hr, outro.min, outro.segs)

    def __lt__(self, outro):
        return (self.hr, self.min, self.segs) < (outro.hr, outro.min, outro.segs)
    

# Testes
r0 = Relogio(25, 30, 30)
r1 = Relogio(14, 45, 15)
r2 = Relogio(6, 20, 40)

print(r1)
print(r2)

r3 = r1 + r2
print(r3)

r4 = r3 - r2 
print(r4)

r4 = r2 - r3
print(r4)

print(r1 == r2)
print(r1 == Relogio(14, 45, 15))
print(r3 > r3)
print(r3 > r2)
print(r2 > r3)
print(r1 < r2)
