# Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

def celsius_to_farenheint (temp):
    return (9 * temp + 160) / 5

# Entrada
C =  float(input("Digite o valor da temperatura em °C: "))

# Processamento (Conversão)
F =  celsius_to_farenheint (C)

# Saída
print(f"O valor da temperatura em Fareheint (°F) é: {F:.2f} °F ")