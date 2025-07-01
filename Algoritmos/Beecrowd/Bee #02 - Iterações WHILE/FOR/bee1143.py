def main():

    n = int(input())

    numero_atual =1

    for _ in range(n):
        quadrado = numero_atual ** 2
        cubo = numero_atual ** 3

        print(numero_atual, quadrado, cubo)

        numero_atual += 1
        
if __name__ == '__main__':
    main()