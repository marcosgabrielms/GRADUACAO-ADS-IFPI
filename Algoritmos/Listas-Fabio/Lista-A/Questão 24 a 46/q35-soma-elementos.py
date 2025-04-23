# Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.:número = 9534 ; soma = 9+5+3+4 = 21.

def soma_elementos (n):
    n1 = n // 1000             # Primeiro dígito
    n2 = (n // 100) % 10        # Segundo dígito
    n3 = (n // 10) % 10         # Terceiro dígito
    n4 = n % 10                 # Quarto dígito
    return (n1) + (n2) + (n3) + (n4)

# Entrada

numero = int(input("Digite um dígito de 4 dígitos: "))

# Processamento

resultado =  soma_elementos(numero)

# Saída

print(f"A soma dos elementos que compõem o número {numero} é igual a {resultado} ")