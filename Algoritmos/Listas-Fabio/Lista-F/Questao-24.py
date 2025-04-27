# Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
# coeficiente A deve ser diferente de 0 (zero).

from io_utils2 import ler_float, escrever
import math

def ler_coeficiente_a():
    a = ler_float("Digite o coeficiente A (diferente de 0): ")
    if a == 0:
        escrever("O coeficiente A não pode ser zero. Tente novamente.")
        return ler_coeficiente_a()
    return a

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        raiz = -b / (2 * a)
        return f"A equação possui uma raiz real: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"As raízes da equação são: {raiz1} e {raiz2}"

def main():
    a = ler_coeficiente_a()
    b = ler_float("Digite o coeficiente B: ")
    c = ler_float("Digite o coeficiente C: ")

    resultado = calcular_raizes(a, b, c)
    escrever(resultado)

if __name__ == "__main__":
    main()
