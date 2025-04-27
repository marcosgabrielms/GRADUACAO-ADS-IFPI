# Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
# escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
# são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
# divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
# escreva o quadrado dos números lidos.

from io_utils2 import ler_inteiro, escrever

def eh_par(numero):
    return numero % 2 == 0

def operacoes(a, b):
    resto = a % b

    if resto == 1:
        resultado = a + b + resto
        escrever(f"Resultado (soma + resto): {resultado}")
    elif resto == 2:
        if eh_par(a):
            escrever(f"{a} é par.")
        else:
            escrever(f"{a} é ímpar.")

        if eh_par(b):
            escrever(f"{b} é par.")
        else:
            escrever(f"{b} é ímpar.")
    elif resto == 3:
        soma = a + b
        resultado = soma * a
        escrever(f"Resultado (soma * primeiro valor): {resultado}")
    elif resto == 4:
        soma = a + b
        if b != 0:
            resultado = soma / b
            escrever(f"Resultado (soma / segundo valor): {resultado}")
        else:
            escrever("Divisão por zero não é permitida.")
    else:
        quadrado_a = a * a
        quadrado_b = b * b
        escrever(f"Quadrado do primeiro número: {quadrado_a}")
        escrever(f"Quadrado do segundo número: {quadrado_b}")

def main():
    a = ler_inteiro("Digite o primeiro número inteiro: ")
    b = ler_inteiro("Digite o segundo número inteiro: ")

    operacoes(a, b)

if __name__ == "__main__":
    main()
