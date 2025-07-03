import sys

def processar_contrados():
    linha_entrada = sys.stdin.readline().strip()
    partes_linha = linha_entrada.split()

    digito_falho_str = partes_linha[0]
    valor_original_str = partes_linha[1]

    while not (digito_falho_str == '0' and valor_original_str == '0'):
        digitos_filtrados = []

        for digito_caractere in valor_original_str:
            if digito_caractere != digito_falho_str:
                digitos_filtrados.append(digito_caractere)

        valor_final_str = "".join(digitos_filtrados)

        if not valor_final_str:
            print(0)
        else: 
            print(int(valor_final_str))

        linha_entrada = sys.stdin.readline().strip()
        partes_linha = linha_entrada.split()
        digito_falho_str = partes_linha[0]
        valor_original_str = partes_linha[1]

if __name__ == '__main__':
    processar_contrados()

