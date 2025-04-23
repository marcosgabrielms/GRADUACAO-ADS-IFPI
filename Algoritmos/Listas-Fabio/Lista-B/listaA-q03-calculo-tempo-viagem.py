# Entrada

distancia = float(input('Digite o valor da distância da viagem(em quilômetros): '))
v_media = float(input('Digite o valor da velocidade média(em Km/h): '))


# Processamento
tempoV = float(distancia / v_media)

# Saída

print(f'O tempo de viagem é de: {tempoV}')