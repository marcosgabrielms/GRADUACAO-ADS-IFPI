def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    original_n1 = n1
    original_n2 = n2

    while n2 != 0:
        n1, n2 = n2, n1 % n2

    print(f"O MDC de {original_n1} e {original_n2} é: {n1}")


main ()