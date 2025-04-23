# Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

def calculo(segundos):
    minutos = segundos / 60
    horas = segundos / 360
    return minutos, horas

#Entrada 
segundos = float(input("Digite um número inteiro de segundos: "))

# Processamento
minutos, horas = calculo(segundos)

# Saída
print(f"{segundos:.2f} segundos equivalem a {horas:.2f} horas e {minutos:.2f} minutos")