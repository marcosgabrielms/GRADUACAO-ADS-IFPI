def ponto_do_meio():

    n = int(input())

    pontos_por_lado = (2 ** n) + 1

    total_pontos_unicos =  pontos_por_lado * pontos_por_lado

    print(total_pontos_unicos)

if __name__ == '__main__':
    ponto_do_meio()

