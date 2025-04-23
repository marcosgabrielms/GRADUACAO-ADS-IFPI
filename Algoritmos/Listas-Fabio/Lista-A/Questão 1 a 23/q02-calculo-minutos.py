#Leia um valor em horas e um valor em minutos, 
#calcule e escreva o equivalente em minutos.
# Entrada
horas = int(input('Digite o valor das horas: '))
minutos = int(input('Digite o valor dos minutos Minutos: '))

# Processamento
# PEMDAS
total_minutos = (horas*60) + minutos

# Saída
print(f'{horas}h 5{minutos}min ==> {total_minutos}min')
