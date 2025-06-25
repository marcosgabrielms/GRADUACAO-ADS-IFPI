def main ():
    valor1 = float(input())
    valor2 = float(input())
    valor3 = float(input())
    valor4 = float(input())
    valor5 = float(input())
    valor6 = float(input())

    positivo = 0
    somatorio = 0

    if valor1 > 0:
       positivo += 1
       somatorio += valor1
    if valor2 > 0:
        positivo += 1
        somatorio += valor2
    if valor3 > 0:
        positivo += 1
        somatorio += valor3
    if valor4 > 0:
        positivo += 1
        somatorio += valor4
    if valor5 > 0:
        positivo += 1
        somatorio += valor5
    if valor6 > 0:
        positivo += 1
        somatorio += valor6
    media = (somatorio / positivo)

    print(f"{positivo} valores positivos")
    print(f"{media:.1f}")


if __name__ == '__main__':
    main()