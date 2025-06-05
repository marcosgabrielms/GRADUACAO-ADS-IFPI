def main():

    x = int(input("Digite o valor de X: "))
    n = int(input("Digite o valor de N sendo >=2: "))

    while n >= 2:
        resultado = x /n
        print(f"{x} dividido por {n} = {resultado}")
        x = resultado
        n -= 1

main()