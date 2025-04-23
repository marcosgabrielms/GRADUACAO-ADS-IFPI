# Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

# Entrada
velocidade = float(input('Digite o valor da velocidade em (km/h): '))
# Processamento
conversao = velocidade / 3.6
# Saída
print(f'O valor da velocidade {velocidade}km/h em m/s é {conversao:.2f} m/s \n')