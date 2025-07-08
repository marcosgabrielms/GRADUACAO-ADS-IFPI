def main():

    maior_palavra_geral = ''

    linha = input().strip()

    while linha != "0":
        palavras = linha.split()
        tamanhos = []

        for palavra in palavras:
            tamanhos.append(str(len(palavra)))

            if len(palavra) > len(maior_palavra_geral):
                maior_palavra_geral = palavra
            elif len(palavra) == len(maior_palavra_geral):
                maior_palavra_geral = palavra
        
        print("-".join(tamanhos))
        linha = input().strip()

    print(f"\nThe biggest word: {maior_palavra_geral}")

if __name__ == '__main__':
    main()