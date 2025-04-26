# Leia 3 (três) números e escreva-os em ordem crescente.

import io_utils

def main():
    num1= io_utils.ler_numero("\nDigite o primeiro número: ")
    num2= io_utils.ler_numero("\nDigite o segundo número: ")
    num3= io_utils.ler_numero("\nDigite o terceiro número: ")

    io_utils.ordenar_numeros(num1, num2, num3)

if __name__ == "__main__":
    main()