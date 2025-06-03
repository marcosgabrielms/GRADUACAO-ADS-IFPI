# Copie o loop de “Raízes quadradas”, na página 111, 
# e encapsule-o em uma função chamada mysqrt que receba a como parâmetro, 
# escolha um valor razoável de x e devolva uma estimativa da raiz quadrada de a.

import math

def mysqrt(a):

    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo")
    if a == 0:
        return 0
    x = a / 2.0 if a != 0 else 1.0
    epsilon = 0.0000001

    while True:
        y = (x + a / x) / 2
        if abs (y - x) < epsilon:
            break
        x = y
    return y

def test_square_root():

    print("a    mysqrt(a)              math.sqrt(a)")
    print("--- ---------------- -------------------- ")

    for a in range(1, 10):
        sqrt_mysqrt = mysqrt(float(a))
        sqrt_math = math.sqrt(float(a))
        diff = abs(sqrt_mysqrt - sqrt_math)
        print(f"{a:<9.1f} {sqrt_mysqrt:<16.11f} {sqrt_math:<16.11f} {diff:<8.1e}")

# Executando a função de teste
test_square_root()