import sys

def contar_aliteracoes_na_linha(linha_de_texto):
    palavras = linha_de_texto.lower().split()

    if len(palavras) < 2:
        return 0

    contador_de_aliteracoes = 0
    em_sequencia_de_aliteracao = False

    indice = 1

    while indice < len(palavras):
        letra_palavra_anterior = palavras[indice - 1][0]
        letra_palavra_atual = palavras[indice][0]

        if letra_palavra_atual == letra_palavra_anterior:
            if not em_sequencia_de_aliteracao:
                contador_de_aliteracoes += 1
                em_sequencia_de_aliteracao = True
        else:
            em_sequencia_de_aliteracao = False

        indice += 1  

    return contador_de_aliteracoes

def processar_entrada(todas_as_linhas):
    for linha in todas_as_linhas:
        linha = linha.strip()
        if linha == "":
            continue
        resultado = contar_aliteracoes_na_linha(linha)
        print(resultado)

if __name__ == '__main__':
    try:
        linhas = []
        while True:
            linha = input()
            if linha.strip() == "":
                break
            linhas.append(linha)
    except EOFError:
        pass

    processar_entrada(linhas)
