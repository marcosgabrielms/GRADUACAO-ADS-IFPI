def main():

    n = int(input())

    for _ in range(n):
        n1, n2, n3 = map(float, input().split())
        n1 = n1 * 2
        n2 = n2 *3
        n3 = n3 * 5
        resultado = (n1 + n2 + n3) / 10
        print(f"{resultado:.1f}")

if __name__ == '__main__':
    main()