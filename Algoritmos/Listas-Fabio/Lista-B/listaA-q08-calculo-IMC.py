# Entrada
peso = float(input('Digite o valor do peso em quilogramas(kg): '))
altura = float(input('Digite o valor do altura em centímetros(cm): '))
# Processamento
imc = ((peso) / (altura**2))
# Saída
print(f'O valor do IMC é {imc:.2f}')