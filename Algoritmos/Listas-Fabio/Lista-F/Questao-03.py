# Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

from io_utils import maior_numero

def main():
    a = int(input("Digite o 1º número e pressione ENTER: "))
    b = int(input("Digite o 2º número e pressione ENTER: "))
    c = int(input("Digite o 3º número e pressione ENTER: "))

    maior = maior_numero(a, b, c)
    print(f"{maior} é o maior número entre os 03 digitados")

main ()        