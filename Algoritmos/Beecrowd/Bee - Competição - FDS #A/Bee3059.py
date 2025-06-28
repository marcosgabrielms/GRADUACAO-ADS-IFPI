import sys

def pares_de_numeros():
    n, i_entrada, f_entrada = map(int, sys.stdin.readline().split())

    vetor = list(map(int, sys.stdin.readline().split()))

    limite_inferior_soma = i_entrada
    limite_superior_soma = f_entrada
    
    contador_pares_validos = 0

    for idx1 in range(n):
        for idx2 in range(idx1 + 1, n):
            soma_par = vetor[idx1] + vetor[idx2]

            if limite_inferior_soma <= soma_par <= limite_superior_soma:
                contador_pares_validos += 1
    
    print(contador_pares_validos)

if __name__ == '__main__':
    pares_de_numeros()