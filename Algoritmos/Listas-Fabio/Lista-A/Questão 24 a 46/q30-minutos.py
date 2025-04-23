# Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.
def calculo_minutos(minutos):
    dias = minutos // (24 * 60) # 1 dia tem 1440 minutos
    resto_minutos = minutos % (24 * 60)
    horas = resto_minutos // 60 # 1d = 24h
    minutos_restantes = resto_minutos % 60 # minutos finais
    return dias, horas, minutos_restantes
    
# Entrada 
minutos = int(input("Digite um número inteiro de minutos "))

# Processamento]
dias, horas, minutos_restantes = calculo_minutos(minutos)

# Saída
print(f"{minutos} minutos equivalem a {dias} dia(s), {horas} horas e {minutos_restantes} minuto(s)")