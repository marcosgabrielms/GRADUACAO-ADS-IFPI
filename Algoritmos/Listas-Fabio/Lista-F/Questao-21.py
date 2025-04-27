# Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
# maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
# contrario, é arredondado para o inteiro imediatamente inferior.

from io_utils2 import ler_float, escrever

def arredondar(numero):
    if numero - int(numero) >= 0.5:
        return int(numero) + 1
    else:
        return int(numero)

def main():
    numero = ler_float("Digite um número para arredondar: ")

    numero_arredondado = arredondar(numero)
    escrever(f"Numero arredondado: {numero_arredondado}")

if __name__ == "__main__":
    main()
