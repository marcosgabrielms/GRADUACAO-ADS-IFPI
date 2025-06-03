# Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.

import io_utils

def main():
    numero = io_utils.ler_numero()
    io_utils.verificar_digitos(numero)

if __name__ == "__main__":
    main()

