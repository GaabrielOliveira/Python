# Receber dois naturais e retornar seu MMC, usando a função mmc do exercício anterior como base.

import Ex5Cap14

def mmc(a, b):
    return a * b / Ex5Cap14.mdc(a, b)

print("Digite dois números naturais")
x = int(input( ))
y = int(input( ))
resultado = mmc(x, y)
print( f"o mmc de {x} e {y} é {resultado}")