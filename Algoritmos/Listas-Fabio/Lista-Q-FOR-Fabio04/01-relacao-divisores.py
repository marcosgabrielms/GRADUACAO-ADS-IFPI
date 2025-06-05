def main():
    while True:
        numero = int(input("\nDigite um número ou pressione 0 para sair: "))

        if numero == 0:
            break  # Flag para encerrar o programa

        print(f"\nNúmero: {numero}")
        print("Divisores:", end=" ")

        # Usando os 3 parâmetros do range: início=1, fim=numero+1, passo=1
        for i in range(1, numero + 1, 1):
            if numero % i == 0:
                print(i, end=" ")

        print("\n")  # quebra de linha após os divisores

main()
