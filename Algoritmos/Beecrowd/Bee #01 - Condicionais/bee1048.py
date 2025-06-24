def main ():
    salario = float(input())
    reajuste = 0
    porcentagem_reajuste = 0

    if salario > 0.0 and salario <= 400.00:
        reajuste = salario * 0.15
        porcentagem_reajuste = 15

    elif salario <= 800.00:
        reajuste = salario * 0.12
        porcentagem_reajuste = 12

    elif salario <= 1200.00:
        reajuste = salario * 0.10
        porcentagem_reajuste = 10

    elif salario <= 2000.00:
        reajuste = salario * 0.07
        porcentagem_reajuste = 7

    elif salario > 2000.00:
        reajuste = salario * 0.04
        porcentagem_reajuste = 4
    
    print(f"Novo salario: {salario + reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {porcentagem_reajuste:}%")

if __name__ == '__main__':
    main()