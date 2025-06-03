# Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

from io_utils import ler_inteiro, escrever

def ler_lista_numeros(quantidade, numeros=None):
    if numeros is None:
        numeros = []
    
    if quantidade == 0:
        return numeros
    else:
        numero = ler_inteiro(f"Digite o número {len(numeros)+1}: ")
        numeros.append(numero)
        return ler_lista_numeros(quantidade - 1, numeros)

def calcular_media(numeros, indice=0, soma=0):
    if indice == len(numeros):
        return soma / len(numeros)
    else:
        soma += numeros[indice]
        return calcular_media(numeros, indice + 1, soma)

def imprimir_maiores_que_media(numeros, media, indice=0):
    if indice == len(numeros):
        return
    else:
        if numeros[indice] > media:
            escrever(f"{numeros[indice]} é maior que a média.")
        return imprimir_maiores_que_media(numeros, media, indice + 1)

def main():
    numeros = ler_lista_numeros(5)
    media = calcular_media(numeros)
    
    escrever(f"A média dos números é {media:.2f}")
    escrever("Números maiores que a média:")
    imprimir_maiores_que_media(numeros, media)

if __name__ == "__main__":
    main()
