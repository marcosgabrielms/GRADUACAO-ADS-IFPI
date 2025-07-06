def main():

    x = []

    for i in range(10):
        valor = int(input())
        if valor <= 0:
            x.append(1)
        else:
            x.append(valor)

    for i in range(10):
        print(f"X[{i}] = {x[i]}")

if __name__ == '__main__':
    main()