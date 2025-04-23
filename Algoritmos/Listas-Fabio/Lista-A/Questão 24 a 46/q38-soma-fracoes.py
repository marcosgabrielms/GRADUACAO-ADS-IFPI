# Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

def fracoes_soma(n1, d1, n2, d2):
    numerdaor = n1 * d2 + n2 * d1
    denominador = d1 * d2
    return numerdaor, denominador
# Entrada
n1 = int(input("Digite o valor do numerador 1: "))     # 1º Fração
d1 = int(input("Digite o valor do denominador 1: "))   # 1º Fração
n2 = int(input("Digite o valor do numerador 2: "))     # 2º Fração
d2 = int(input("Digite o valor do denominador 2: "))   # 2º Fração

# Processamento

num, den = fracoes_soma(n1, d1, n2, d2)

# Saída

print(f"A soma das frações é: {num}/{den}")