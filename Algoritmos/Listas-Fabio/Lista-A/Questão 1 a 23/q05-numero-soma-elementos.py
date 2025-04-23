# Leia um número inteiro (3 dígitos), 
# calcule e escreva a soma de seus elementos (C + D + U).

# Entrada
numero = int(input('Digite um número de três dígitos: '))

# Processamento
c = numero // 100
d = (numero // 10) % 10
u = numero % 10

# Saída
print(f'A soma dos elementos Centena, Dezena e Unidade do número {numero} é igual a {c + d +u}:  ' )