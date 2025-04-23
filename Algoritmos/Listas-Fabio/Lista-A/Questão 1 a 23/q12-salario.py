# Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.

def novo_salario (salario):

    return salario * 1.25

# Entrada
salario = float(input('Digite o valor do salário em reais: '))

# Saída
print("O novo salário com aumento de 25% é: R$",novo_salario(salario))

