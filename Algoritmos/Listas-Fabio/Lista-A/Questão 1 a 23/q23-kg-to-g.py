# Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama).
def kg_to_g (valor):
    return valor * 1000

# Entrada
kg = float(input("Digite o valor em quilogramas (kg): "))

# Processamento
resultado = kg_to_g (kg)

# Saída
print(f"O valor de {kg} quilogramas em gramas é: {resultado} g ")