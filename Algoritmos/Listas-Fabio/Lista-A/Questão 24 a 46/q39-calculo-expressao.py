# Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:

def calculo_expressao(A, B, C):
    R = (A + B) ** 2
    S = (B + C) ** 2
    D = (R + S) // 2
    return D

# Entrada
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

# Procesamento

calculo = calculo_expressao(A, B, C)

# Saída 
print(f" O calculo da expressão D = (R + S) / 2 , sendo R = (A + B)^2 e S (B + C)^2 é: {calculo}")
