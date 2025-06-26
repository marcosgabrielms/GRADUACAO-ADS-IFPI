def main():

    x = int(input())

    for numero in range (1, x + 1):
        if numero % 2 != 0:
            print(numero)

if __name__ == '__main__':
    main()