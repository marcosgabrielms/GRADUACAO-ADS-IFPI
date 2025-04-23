# Escreva um programa que determine a quantidade de notas de 50 e 10 necessárias para um determinado valor. 

# Entrada

valor = float(input('Digite a quantia em Reais:'))


# Processamento

nota50 = int(valor // 50)
resto = valor % 50
nota10 = int(resto // 10)

# Saída
print(f'{valor} reais são {nota50} nota(s) de R$ 50,00 e {nota10} nota(s) de R$ 10,00 ')