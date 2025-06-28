def main():

    n = int(input())
    total_coelhos = 0
    total_sapos = 0
    total_ratos = 0
    total_geral_cobaias = 0

    for _ in range(n):
        entrada = input().split()
        quantidade = int(entrada[0])
        tipo = entrada[1]
        
        if tipo == 'C':
            total_coelhos += quantidade
        elif tipo == 'S':
            total_sapos += quantidade
        else:
            total_ratos += quantidade

        total_geral_cobaias += quantidade

    percentual_coelhos = (total_coelhos / total_geral_cobaias) * 100    
    percentual_sapos = (total_sapos / total_geral_cobaias) * 100    
    percentual_ratos = (total_ratos / total_geral_cobaias) * 100    

    print(f"Total: {total_geral_cobaias} cobaias")
    print(f"Total de coelhos: {total_coelhos}")
    print(f"Total de ratos: {total_ratos}")
    print(f"Total de sapos: {total_sapos}")
    print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
    print(f"Percentual de ratos: {percentual_ratos:.2f} %")
    print(f"Percentual de sapos: {percentual_sapos:.2f} %")

if __name__ == '__main__':
    main()