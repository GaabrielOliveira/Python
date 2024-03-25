# Receber dois naturais e retornar seu MDC.
def mdc(a, b):
    mdc_atual = 1
    for divisor in range(2, a + 1):
        if a % divisor == 0 and b % divisor == 0:
            mdc_atual = divisor
    return mdc_atual

if __name__ == "__main__":
    print("Digite dois números naturais: ")
    x = int(input( ))
    y = int(input( ))
    resultado = mdc(x, y)
    print( f"o mdc de {x} e {y} é {resultado}")