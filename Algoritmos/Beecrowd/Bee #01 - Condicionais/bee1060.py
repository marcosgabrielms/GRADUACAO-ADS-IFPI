def main ():
    valor1 = float(input())
    valor2 = float(input())
    valor3 = float(input())
    valor4 = float(input())
    valor5 = float(input())
    valor6 = float(input())

    positivo = 0

    if valor1 > 0:
       positivo += 1
    if valor2 > 0:
        positivo += 1
    if valor3 > 0:
        positivo += 1
    if valor4 > 0:
        positivo += 1
    if valor5 > 0:
        positivo += 1
    if valor6 > 0:
        positivo += 1
        
    print(f"{positivo} valores positivos")


if __name__ == '__main__':
    main()