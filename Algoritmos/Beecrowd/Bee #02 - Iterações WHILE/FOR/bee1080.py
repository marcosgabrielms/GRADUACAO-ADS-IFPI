def main():

    maior_valor_encontrado = int(input())
    posicao_do_maior = 1

    for posicao_atual in range(2, 101):
        numero_lido = int(input())

        if numero_lido > maior_valor_encontrado:
            maior_valor_encontrado = numero_lido
            posicao_do_maior = posicao_atual
          

    print(maior_valor_encontrado)
    print(posicao_do_maior)

if __name__ == '__main__':
    main()