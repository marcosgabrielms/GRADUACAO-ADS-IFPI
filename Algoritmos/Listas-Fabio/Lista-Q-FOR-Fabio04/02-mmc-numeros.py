def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    maior = max(n1, n2)
    limite = n1 * n2  # Valor máximo possível do MMC

    for candidato in range(maior, limite + 1, 1):  # Começa no maior, vai até n1*n2
        if candidato % n1 == 0 and candidato % n2 == 0:
            print(f"O MMC de {n1} e {n2} é: {candidato}")
            break

main()
