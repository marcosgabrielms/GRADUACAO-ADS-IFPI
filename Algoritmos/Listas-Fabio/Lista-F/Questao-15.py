#Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
# Escreva na tela qual dos professores tem salário total maior.

from io_utils import ler_inteiro, ler_float, escrever

def calcular_salario(horas, valor_por_hora):
    return horas * valor_por_hora

def comparar_salarios(salario1, salario2):
    if salario1 > salario2:
        return "O professor 1 tem o salário maior."
    elif salario2 > salario1:
        return "O professor 2 tem o salário maior."
    else:
        return "Os dois professores têm salários iguais."

def main():
    horas1 = ler_inteiro("Digite a quantidade de horas/aula do professor 1: ")
    valor1 = ler_float("Digite o valor por hora do professor 1: ")

    horas2 = ler_inteiro("Digite a quantidade de horas/aula do professor 2: ")
    valor2 = ler_float("Digite o valor por hora do professor 2: ")

    salario1 = calcular_salario(horas1, valor1)
    salario2 = calcular_salario(horas2, valor2)

    resultado = comparar_salarios(salario1, salario2)
    escrever(resultado)

if __name__ == "__main__":
    main()
