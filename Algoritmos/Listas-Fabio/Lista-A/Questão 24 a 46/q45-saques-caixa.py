# Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o numero de notas de cada valor que deve ser disponibilizado 
# para o cliente que realizou o saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas 
# em número mínimo possível. Por exemplo, se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, 
# o algoritmo deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que receba o valor da 
# quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.

def distribuir_notas(valor):
    nota50 = valor // 50
    valor = valor % 50
    nota10 = valor // 10
    valor = valor % 10
    nota5 = valor // 5
    valor = valor % 5
    nota1 = valor
    return nota50, nota10, nota5, nota1

# Entrada
valor_saque = int(input("Digite o valor a ser sacado: "))

# Processamento
n50, n10, n5, n1 = distribuir_notas(valor_saque)

# Saída
print("Distribuição das notas:")
print(f"{n50} nota(s) de R$50")
print(f"{n10} nota(s) de R$10")
print(f"{n5} nota(s) de R$5")
print(f"{n1} nota(s) de R$1")
