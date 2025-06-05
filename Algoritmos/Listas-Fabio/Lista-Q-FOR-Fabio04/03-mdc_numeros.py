def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    menor = min(n1, n2)  # pega o menor entre n1 e n2
    mdc = 1  # começa assumindo que o MDC mínimo é 1

    for i in range(1, menor + 1, 1):  # start=1, limit=menor+1, step=1
        if n1 % i == 0 and n2 % i == 0:
            mdc = i  # atualiza o MDC se i divide os dois

    print(f"O MDC de {n1} e {n2} é: {mdc}")

main()
