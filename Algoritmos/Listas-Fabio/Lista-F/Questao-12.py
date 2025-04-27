# Leia 1 (um) número inteiro e escreva se este número é par ou impar.

from io_utils import ler_inteiro, escrever

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    numero = ler_inteiro("Digite um número inteiro: ")
    resultado = verificar_par_impar(numero)
    escrever(f"O número {numero} é {resultado}.")

if __name__ == "__main__":
    main()
