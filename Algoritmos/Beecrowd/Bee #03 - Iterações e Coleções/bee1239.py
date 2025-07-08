import sys 

def traduzir_linha_para_html(linha_texto):

    em_italico = False
    em_negrito = False
    partes_saida = []

    for caractere in linha_texto:
        if caractere == '_':
            if not em_italico:
                partes_saida.append('<i>')
                em_italico = True
            else:
                partes_saida.append('</i>')
                em_italico = False

        elif caractere == '*':
            if not em_negrito:
                partes_saida.append('<b>')
                em_negrito = True
            else:
                partes_saida.append('</b>')
                em_negrito = False
        else:
            partes_saida.append(caractere)
    return "".join(partes_saida)

def main():
    
    for linha in sys.stdin:
        linha_limpa = linha.rstrip('\n')

        linha_traduzida = traduzir_linha_para_html(linha_limpa)
        print(linha_traduzida)

if __name__ == '__main__':
    main()