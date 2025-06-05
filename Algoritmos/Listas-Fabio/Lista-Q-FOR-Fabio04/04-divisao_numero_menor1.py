def main():
    numero = int(input("Digite um número: "))
    resultados = []

    for n in range(numero, 1, -1):  # começa do número, vai até >1, descendo
        if n % 2 == 0:  # só divide se for número par (senão não segue a lógica da divisão exata por 2)
            resultados.append(n)
            numero = n // 2
        else:
            break

    for i in range(len(resultados)):
        if i == len(resultados) - 1:
            print(f"{resultados[i]}")
        else:
            print(f"{resultados[i]} ÷ 2 -> ", end="")

    print(f"O último resultado maior ou igual a 1 foi: {resultados[-1]}")

main()
