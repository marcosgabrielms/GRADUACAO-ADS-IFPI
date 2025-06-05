def main():
    numero = int(input("Digite um número: "))
    numero_inicial = abs(numero)  # usa valor absoluto para evitar número negativo
    qtd_digitos = 0

    for _ in range(len(str(numero_inicial))):  # usando for com a quantidade de dígitos da string
        qtd_digitos += 1

    # Garante que zero tem 1 dígito
    if numero_inicial == 0:
        qtd_digitos = 1

    print(f"O número {abs(numero)} tem: {qtd_digitos} dígito(s)")

main()
