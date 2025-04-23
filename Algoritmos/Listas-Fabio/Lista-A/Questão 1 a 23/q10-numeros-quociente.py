# Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1º pelo 2º

# Entrada
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

# Processamento
quociente = (n1 / n2) % n1
resto = n1 % n2
# Saída

print(f'Quociente {quociente}')
print(f'Resto {resto}')
