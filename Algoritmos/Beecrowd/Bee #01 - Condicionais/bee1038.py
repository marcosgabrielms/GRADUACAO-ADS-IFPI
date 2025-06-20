def main():
    codigo = int(input())
    quantidade = int(input())

    if codigo == 1:
        conta = quantidade * 4.00
        print(f"Total: R$ {conta:.2f}")
    elif codigo == 2:
        conta = quantidade * 4.50
        print(f"Total: R$ {conta:.2f}")
    elif codigo == 3:
        conta = quantidade * 5.00
        print(f"Total: R$: {conta:.2f}")
    elif codigo == 4:
        conta = quantidade * 2.00
        print(f"Total R$: {conta:.2f}")
    elif codigo == 5:
        conta = quantidade * 1.50
        print(f"Total R$: {conta:.2f}")

if __name__ == '__main__':
    main()
