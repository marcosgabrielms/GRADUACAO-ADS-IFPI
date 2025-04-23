# Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

def farenheint_to_celsius (temp):
    return (5 * temp - 160) / 9

# Entrada
F =  float(input("Digite o valor da temperatura em Farenheint (°F): "))

# Processamento (Conversão)
C = farenheint_to_celsius (F)

# Saída
print(f"O valor da temperatura em grau celsius (°C) é: {C:.2f} °F ")