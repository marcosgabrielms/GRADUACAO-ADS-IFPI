import sys

def obter_numero_processado(texto_original: str) -> str:
    digitos_filtrados = []

    for caractere in texto_original:
        if caractere == ',' or caractere == ' ':
            continue
        elif caractere == 'O' or caractere == 'o': 
            digitos_filtrados.append('0')
        elif caractere == 'l': 
            digitos_filtrados.append('1')
        elif '0' <= caractere <= '9':
            digitos_filtrados.append(caractere)
        else:
            return ""
            
    return "".join(digitos_filtrados)

def principal(): 
    valor_maximo_int_32_bits = 2147483647 

    for linha_entrada in sys.stdin:
        linha_entrada = linha_entrada.strip()

        string_do_numero = obter_numero_processado(linha_entrada)

        if not string_do_numero:
            print("error")
            continue

        numero_final = int(string_do_numero)

        if numero_final > valor_maximo_int_32_bits:
            print("error")
        else:
            print(numero_final)

if __name__ == '__main__':
    principal() 