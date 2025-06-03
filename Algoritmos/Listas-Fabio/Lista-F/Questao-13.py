# Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
# diferentes.

from io_utils import ler_inteiro, escrever

def ler_lista_numeros(quantidade, numeros=None):
    if numeros is None:
        numeros = []
    
    if quantidade == 0:
        return numeros
    else:
        numero = ler_inteiro(f"Digite o número {len(numeros)+1}: ")
    
        if numero in numeros:
            escrever("Número repetido! Digite um número diferente.")
            return ler_lista_numeros(quantidade, numeros)
        else:
            numeros.append(numero)
            return ler_lista_numeros(quantidade - 1, numeros)

def encontrar_maior(numeros, indice=0, maior=None):
    if maior is None:
        maior = numeros[0]
    
    if indice == len(numeros):
        return maior
    else:
        if numeros[indice] > maior:
            maior = numeros[indice]
        return encontrar_maior(numeros, indice + 1, maior)

def encontrar_menor(numeros, indice=0, menor=None):
    if menor is None:
        menor = numeros[0]
    
    if indice == len(numeros):
        return menor
    else:
        if numeros[indice] < menor:
            menor = numeros[indice]
        return encontrar_menor(numeros, indice + 1, menor)

def main():
    numeros = ler_lista_numeros(5)
    
    maior = encontrar_maior(numeros)
    menor = encontrar_menor(numeros)
    
    escrever(f"O maior número é {maior}")
    escrever(f"O menor número é {menor}")

if __name__ == "__main__":
    main()
