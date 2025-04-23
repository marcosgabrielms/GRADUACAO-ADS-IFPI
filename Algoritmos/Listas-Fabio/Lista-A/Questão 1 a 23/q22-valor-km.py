# Leia um valor em km, calcule e escreva o equivalente em m.

def km_to_m (valor):
    return valor * 1000

# Entrada
km = float(input("Digite o valor em quilômetros(km): "))

# Processamento
resultado = km_to_m (km)

# Saída
print(f"O valor de {km} Km para metros é {resultado} m ")