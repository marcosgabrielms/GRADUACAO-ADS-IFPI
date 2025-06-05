def main():
    x = int(input("Digite o valor de X: "))
    n = int(input("Digite o valor de N sendo >= 2: "))

    for i in range(n, 1, -1):  # começa em n, vai até 2 (exclui o 1), de -1 em -1
        resultado = x / i
        print(f"{x} dividido por {i} = {resultado}")
        x = resultado  # atualiza o valor de x para a próxima divisão

main()
