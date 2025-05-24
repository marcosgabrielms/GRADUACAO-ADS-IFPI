def obter_texto(label):
    texto =  input(label).strip()
    return texto

def obter_tamanho_minimo(label, tamanho_minimo):
    while True:
        texto =  input(label).strip()
        if len(texto) >= tamanho_minimo:
            return texto
        print(f"Texto muito curto, digite pelo menos um texto de tamanho {tamanho_minimo} caracteres")

def obter_texto_tamanho_maximo(label, tamanho_maximo):
    while True:
        texto = input(label).strip()
        if len(texto) <= tamanho_maximo:
            return texto
        print(f"Texto muito longo, pelo menos um texto de tamanho {tamanho_maximo} caracteres")        

def obter_texto_tamanho_faixa(label, minimo, maximo):
    if minimo > maximo:
        print(f"Erro: O valor mínimo {minimo} não pode ser maior que o valor máximo {maximo}")
        return
    while True:
        texto = input(label).strip()
        if minimo <= len(texto) <= maximo:
            return texto
        print(f"O texto deve ter entre {minimo} e {maximo} caracteres. ")



def main():
    # texto = obter_tamanho_minimo("Digite um texto com no mínimo 10 caracteres: ", 10)
    # texto = obter_tamanho_minimo("Digite um texto com no máximo 50 caracteres: ", 50)
    texto = obter_texto_tamanho_faixa("Digite uma frase entre 10 e 20 caracteres: ", 10, 50)
    print(f'Texto digitado {texto}')

if __name__ == '__main__':
    main()