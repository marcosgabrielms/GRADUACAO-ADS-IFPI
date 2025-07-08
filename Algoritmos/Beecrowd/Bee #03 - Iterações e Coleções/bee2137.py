def main():
    while True:
        try:
            n = int(input())

            codigos = []

            for _ in range(n):
                codigos.append(input())

            codigos.sort()

            for codigo in codigos:
                print(codigo)

        except EOFError:
            break

if __name__ == '__main__':
    main()