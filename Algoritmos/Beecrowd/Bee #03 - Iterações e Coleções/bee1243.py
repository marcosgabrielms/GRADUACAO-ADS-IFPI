import sys

def eh_palavra_valida(token_original):
    token_analisado = token_original
    
    if token_analisado.endswith('.'):
        token_analisado = token_analisado[:-1]
    
    if token_analisado and token_analisado.isalpha():
        comprimento = len(token_analisado)
        return (True, comprimento)
    
    return (False, 0)

def processa_linhas_e_calcula_pontos(lista_de_linhas):
    for linha in lista_de_linhas:
        tokens = linha.split()
        
        soma_dos_comprimentos = 0
        quantidade_de_palavras_validas = 0
        
        for token in tokens:
            eh_valida, comprimento = eh_palavra_valida(token)
            
            if eh_valida:
                soma_dos_comprimentos += comprimento
                quantidade_de_palavras_validas += 1
        
        media_comprimento = 0
        if quantidade_de_palavras_validas > 0:
            media_comprimento = soma_dos_comprimentos // quantidade_de_palavras_validas
            
        if media_comprimento <= 3:
            print(250)
        elif media_comprimento <= 5:
            print(500)
        else:
            print(1000)

if __name__ == '__main__':
    linhas_da_entrada = sys.stdin.readlines()
    processa_linhas_e_calcula_pontos(linhas_da_entrada)