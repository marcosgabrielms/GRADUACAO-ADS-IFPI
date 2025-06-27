def main():

    n = int(input())

    for numero_atual in range(1, n +1):
        if numero_atual % 2 == 0:
            resultado_quadrado = numero_atual ** 2

            print(f"{numero_atual}^2 = {resultado_quadrado}")

if __name__ == '__main__':
    main()