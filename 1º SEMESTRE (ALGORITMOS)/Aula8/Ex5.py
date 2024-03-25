# Dados três inteiros, a soma deles é ímpar? Responda com SIM ou NÃO.

n1 = int(input( "Digite um numero: " ))
n2 = int(input( "Digite um numero: " ))
n3 = int(input( "Digite um numero: " ))

m = n1 + n2 + n3

if m % 2 == 0:
    print("Não, a soma dos numeros é par")
else:
    print("Sim, a soma dos numeros é impar")