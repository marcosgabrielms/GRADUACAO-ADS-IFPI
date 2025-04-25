# Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

from io_utils import maior_e_menor

def main():
    a = int(input("Digite o 1º número e pressione ENTER: "))
    b = int(input("Digite o 2º número e pressione ENTER: "))

    maior, menor = maior_e_menor(a, b)

    if a == b:
        print("Os dois números são iguais:", a)
    else:
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")

main ()        