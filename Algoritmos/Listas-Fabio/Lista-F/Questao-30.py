# Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
# o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
# milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
# terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
# 2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.

from io_utils2 import ler_inteiro, escrever

def ler_numero_quatro_digitos():
    numero = ler_inteiro("Digite um número de 4 dígitos: ")

    if numero < 1000 or numero > 9999:
        escrever("Número inválido. Deve ter exatamente 4 dígitos.")
        return ler_numero_quatro_digitos()

    return numero

def verificar_caracteristica(numero):
    parte_esquerda = numero // 100
    parte_direita = numero % 100

    soma = parte_esquerda + parte_direita
    quadrado = soma * soma

    return quadrado == numero

def main():
    numero = ler_numero_quatro_digitos()

    if verificar_caracteristica(numero):
        escrever(f"O número {numero} obedece à característica especial!")
    else:
        escrever(f"O número {numero} NÃO obedece à característica especial.")

if __name__ == "__main__":
    main()
