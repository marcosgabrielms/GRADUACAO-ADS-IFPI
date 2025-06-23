def main():
    a, b = map(int, input().split())

    if (b != 0 and a % b == 0) or (a != 0 and b % a == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

if __name__ == '__main__':
    main()