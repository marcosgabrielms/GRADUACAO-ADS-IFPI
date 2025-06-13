def gerar_pa_recursiva(termo_atual, limite, r):
    
    #Caso Base(condição de parada)

    if termo_atual >= limite:
        return   # -> Se o termo atual atingiu ou ultrapassou o limite, a função para
    print(termo_atual)   # Ação
    gerar_pa_recursiva(termo_atual + r,  limite, r)   # A função chama a si mesma, passando o próximo termo da progressão


def main():
    
    try:
        a0 = int(input("Digite o valor inicial de (A0): "))
        limite =  int(input("Digite o valor do limite: "))
        r = int(input("Digite o valor da razão (R): "))

        if r <= 0:
            print("\nErro, a razão (R) deve ser um númeor positivo maior que zero")
        else:
            print(f"\n-----Valores da PA menores que {limite}-----")
            gerar_pa_recursiva(a0,limite,r)
            print("-------------------------------------------")
    except ValueError:
        print("\nErro, por favor, digite apenas números inteiros válidos")
    
main()
