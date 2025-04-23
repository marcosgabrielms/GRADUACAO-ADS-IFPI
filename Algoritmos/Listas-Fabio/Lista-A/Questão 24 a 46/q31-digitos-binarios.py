# Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

def binarios_to_decimal (n):
    n1 = n // 1000            # Primeiro dígito
    n2 = (n // 100) % 10        # Segundo dígito
    n3 = (n // 10) % 10         # Terceiro dígito
    n4 = n % 10                 # Quarto dígito
    return (n1 * 2**3) + (n2 * 2**2) + (n3 * 2**1) + (n4 * 2**0)

# Entrada

n_binario = int(input("Digite o número binário de 4 dígitos: "))

# Processamento

decimal =  binarios_to_decimal(n_binario)

# Saída

print(f"O número binário {n_binario} equivale {decimal} decimal")