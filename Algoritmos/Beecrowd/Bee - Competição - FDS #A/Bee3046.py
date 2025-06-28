def main ():

    n = int(input())

    calculo_qtd_peças =  ((n + 1) * (n + 2)) / 2

    if 0 <= n <= 10000:
        print(int(calculo_qtd_peças))

if __name__ == '__main__':
    main()