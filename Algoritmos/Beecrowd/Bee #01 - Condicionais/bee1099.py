def main():

    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split())

        if x < y:
            menor_valor = x
            maior_valor = y
        else:
            menor_valor = y
            maior_valor = x

        soma_impares = 0
        for numero in range(menor_valor + 1, maior_valor):
            if numero % 2 != 0:
                soma_impares += numero

        print(soma_impares)

if __name__ == '__main__':
    main()