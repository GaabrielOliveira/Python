# Dados dois números, algum deles é ímpar?

x = int(input( "digite um numero: "))
y = int(input( "digite um numero: "))

if (x % 2 != 0 or y % 2 != 0):
    print("SIM")
else:
    print("NÃO")