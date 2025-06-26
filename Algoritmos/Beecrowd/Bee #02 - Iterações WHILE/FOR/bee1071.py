def main():
    x = int(input())
    y = int(input())

    soma_impares = 0
    inicio_intervalo = 0
    fim_intervalo = 0

    if x < y:
        inicio_intervalo = x
        fim_intervalo = y
    else:
        inicio_intervalo = y
        fim_intervalo = x
    
    for numero_atual in range(inicio_intervalo + 1, fim_intervalo):
        if numero_atual % 2 != 0:
            soma_impares += numero_atual

    print(soma_impares)

if __name__ == '__main__':
    main()