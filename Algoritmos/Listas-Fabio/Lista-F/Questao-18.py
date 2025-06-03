# Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
# Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
# sobre os dois valores lidos.

from io_utils2 import ler_inteiro, ler_float, escrever

def calcular_resultado(valor1, valor2, operacao):
    if operacao == 1:
        return valor1 + valor2
    elif operacao == 2:
        return valor1 - valor2
    elif operacao == 3:
        return valor1 * valor2
    elif operacao == 4:
        if valor2 != 0:
            return valor1 / valor2
        else:
            escrever("Erro: Divisão por zero!")
            return None
    else:
        escrever("Operação inválida.")
        return None

def main():
    valor1 = ler_float("Digite o primeiro valor: ")
    valor2 = ler_float("Digite o segundo valor: ")
    operacao = ler_inteiro("Digite a operação (1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão): ")

    resultado = calcular_resultado(valor1, valor2, operacao)

    if resultado is not None:
        escrever(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
