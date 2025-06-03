# Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
# valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
# possíveis para a variável opção são 1, 2 e 3.


from io_utils import ler_inteiro, escrever

def escolher_numero(opcao, num1, num2, num3):
    if opcao == 1:
        return num1
    elif opcao == 2:
        return num2
    elif opcao == 3:
        return num3
    else:
        
        nova_opcao = ler_inteiro("Opção inválida. Digite 1, 2 ou 3: ")
        return escolher_numero(nova_opcao, num1, num2, num3)

def main():
    opcao = ler_inteiro("Digite a opção (1, 2 ou 3): ")
    num1 = ler_inteiro("Digite o primeiro número: ")
    num2 = ler_inteiro("Digite o segundo número: ")
    num3 = ler_inteiro("Digite o terceiro número: ")

    resultado = escolher_numero(opcao, num1, num2, num3)
    escrever(f"O número escolhido foi: {resultado}")

if __name__ == "__main__":
    main()
