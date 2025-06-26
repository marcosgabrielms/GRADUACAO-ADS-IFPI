def main():

    numero = int(input())
    impares = 0
    numero_atual = numero

    while impares < 6:
        if numero_atual % 2 != 0:
            print(numero_atual)
            impares += 1
        numero_atual += 1

if __name__ == '__main__':
    main()