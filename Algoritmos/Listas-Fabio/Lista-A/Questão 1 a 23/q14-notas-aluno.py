# Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

def media_ponderada(n1, p1, n2, p2, n3, p3):
    return ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3) # Cálculo da Média

n1 = float(input(f'Digite o valor da 1º nota: '))
p1 = float(input(f'Digite o valor do peso 1: '))
n2 = float(input(f'Digite o valor da 2º nota: '))
p2 = float(input(f'Digite o valor do peso 2: '))
n3 = float(input(f'Digite o valor da 3º nota: '))
p3 = float(input(f'Digite o valor do peso 3: '))

resultado = media_ponderada(n1, p1, n2, p2, n3, p3)

print(f"O valor da média ponderada é: {resultado: .2f}")