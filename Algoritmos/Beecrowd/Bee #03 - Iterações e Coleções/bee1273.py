def main():

    primeira_execucao = True

    try:
        n = int(input())
    except (ValueError, EOFError):
        n = 0
    
    while n != 0:

        if not primeira_execucao:
            print()
        
        palavras = []

        for _ in range(n):
            palavras.append(input())
        
        if palavras:
            maior_comprimento = max(len(p) for p in palavras)
        else:
            maior_comprimento = 0

        for palavra in palavras:
            print(palavra.rjust(maior_comprimento))

        primeira_execucao = False

        try:
            n = int(input())
        except (ValueError, EOFError):
            n = 0

if __name__ == '__main__':
    main()