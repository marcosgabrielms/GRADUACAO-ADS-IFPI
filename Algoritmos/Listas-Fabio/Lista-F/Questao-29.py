# Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
# formadas pelos seus dois primeiros e dois últimos dígitos.
# Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
# Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

from io_utils2 import ler_inteiro, escrever
import math

def ler_numero_quatro_digitos():
    numero = ler_inteiro("Digite um número de 4 dígitos: ")

    if numero < 1000 or numero > 9999:
        escrever("Número inválido. Deve ter exatamente 4 dígitos.")
        return ler_numero_quatro_digitos()

    return numero

def verificar_quadrado_perfeito(numero):
    raiz = math.isqrt(numero)  
    if raiz * raiz != numero:
        return False  

    dois_primeiros = numero // 100
    dois_ultimos = numero % 100

    return raiz == (dois_primeiros + dois_ultimos)

def main():
    numero = ler_numero_quatro_digitos()

    if verificar_quadrado_perfeito(numero):
        escrever(f"O número {numero} é um quadrado perfeito especial!")
    else:
        escrever(f"O número {numero} NÃO é um quadrado perfeito especial.")

if __name__ == "__main__":
    main()
