# Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

def inverter_numero (numero):
    
    C = numero // 100 # Centena
    D = (numero // 10) % 10 # Dezena
    U = numero % 10 # Unidade

    return (U * 100) + (D * 10) + C

numero = int(input('Digite um número inteiro de 03 dígitos: '))
print("Número invertido: ", inverter_numero(numero))