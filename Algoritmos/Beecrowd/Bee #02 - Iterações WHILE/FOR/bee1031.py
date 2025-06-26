def main():
    n = int(input())

    while n != 0:
        resultado = encontrar_m(n)
        print(resultado)
        n = int(input())

def encontrar_m(valor_n):
    m = 1
    ultima_estacao_removida = desligamento(valor_n, m)

    while ultima_estacao_removida != 13:
        m += 1
        ultima_estacao_removida = desligamento(valor_n, m)

    return m

def desligamento(n, m):
    regioes = list(range(1, n + 1))

    regioes_desligadas = [] 

    posicao_para_remover = 0 

    regiao_desligada_inicial = regioes.pop(posicao_para_remover)
    regioes_desligadas.append(regiao_desligada_inicial)

    posicao_no_array = posicao_para_remover

    while len(regioes) > 0:
        posicao_para_remover = (posicao_no_array + m - 1) % len(regioes) 

        regiao_desligada = regioes.pop(posicao_para_remover)
        regioes_desligadas.append(regiao_desligada)

        posicao_no_array = posicao_para_remover
        
    return regioes_desligadas[-1] 

if __name__ == '__main__':
    main()