# Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

from io_utils import contar_iguais # importa a função "contar iguais"

def main ():
    a= int(input("Digite o 1º número: "))
    b= int(input("Digite o 2º número: "))
    c= int(input("Digite o 3º número: "))

    resultado = contar_iguais(a, b, c)
    print(resultado)

main()