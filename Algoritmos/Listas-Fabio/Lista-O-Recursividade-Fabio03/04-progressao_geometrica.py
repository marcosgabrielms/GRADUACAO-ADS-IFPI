def gerar_pg_recursiva(termo_atual, limite, r):
    if termo_atual >= limite:
        return
    print(termo_atual)
    gerar_pg_recursiva(termo_atual * r, limite, r) # Chama a função a si mesma, passando para o próximo termo

def main():
    try:
        a0 = int(input("\nDigite o valor inicial de (A0): "))
        limite =  int(input("Digite o valor do limite: "))
        r = int(input("Digite o valor da razão (R): "))

        if r <= 1:
            print("\nErro: o valor da razão tem que ser maior que 1")
        else:
            print(f"\nValores da PG menores que {limite}")
        gerar_pg_recursiva(a0, limite, r)
        print("---------------------------------------")
    except ValueError:
        print("\nErro: digite apenas números inteiros válidos")

main()