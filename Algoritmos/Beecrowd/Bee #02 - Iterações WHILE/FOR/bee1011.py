def main():
    m, n = map(int, input().split())

    while m > 0 and n > 0:
        menor = min(m, n)
        maior = max(m, n)

        soma = 0

        for numero in range(menor, maior + 1):
            print(numero, end=' ')
            soma += numero

        print(f"Sum={soma}")
        m, n = map(int, input().split())

if __name__ == '__main__':
    main()
