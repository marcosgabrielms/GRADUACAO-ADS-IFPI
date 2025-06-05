def main():
    n = int(input("Digite o número alvo: "))

    for _ in range(1000): 
        num = int(input("Digite um número da lista: "))
        if num == n:
            print(f"Número igual ao alvo {n} encontrado.")
            break

main()
