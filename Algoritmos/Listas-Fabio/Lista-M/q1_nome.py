def main ():
    nome = input("Digite o nome: ")
    tamanho = len(nome)
    print(f'O nome tem {tamanho} caracteres')

    if tamanho % 2 == 0:    # par
        print(f'O tamanho {tamanho} é PAR. Múltiplos:')
        contador = 0
        atual = tamanho + tamanho  
        while contador < tamanho:
            print(atual)
            atual = atual + tamanho
            contador += 1
    else: # impar 
        print(f'O tamanho {tamanho} é ÍMPAR. Divisores:')
        candidato = tamanho
        while candidato > 0:
            if tamanho % candidato == 0:
                print(candidato)
            candidato -= 1

main()