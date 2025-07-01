def main():

    n = int(input())

    sequencia = 1

    for _ in range(n):

        print(sequencia, sequencia + 1, sequencia + 2, "PUM")
        sequencia += 4

if __name__ == '__main__':
    main()