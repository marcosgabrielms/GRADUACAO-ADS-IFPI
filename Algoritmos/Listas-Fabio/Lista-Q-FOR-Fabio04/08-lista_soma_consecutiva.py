def main():
    X = int(input("Digite o valor de X: "))

    lista = []
    num = int(input("Digite um número da lista: "))
    lista.append(num)

    for i in range(1, 5, 1):  # start=1, stop=1000, step=1
        proximo = int(input("Digite o próximo número da lista: "))
        lista.append(proximo)

        if lista[-1] + lista[-2] == X:
            break

    print("Números lidos:")
    for n in lista:
        print(n)

main()
