def main():
    X = int(input("Digite o valor de X: "))

    lista = []
    num = int(input("Digite um número da lista: "))
    lista.append(num)

    while True:
        proximo = int(input("Digite o próximo número da lista: "))
        lista.append(proximo)

        
        if lista[-1] + lista[-2] == X: # Verifica se soma dos dois últimos é igual a X
            break

    print("Números lidos:")
    for n in lista:
        print(n)

main()
