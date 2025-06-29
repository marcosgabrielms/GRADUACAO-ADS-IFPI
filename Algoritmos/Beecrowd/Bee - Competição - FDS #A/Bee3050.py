import sys

def distancia_entre_amigos():
    numero_predios = int(sys.stdin.readline())
    alturas_predios = list(map(int, sys.stdin.readline().split()))

    valores_P = [0] * numero_predios
    valores_Q = [0] * numero_predios

    for indice_k in range(numero_predios):
        valores_P[indice_k] = alturas_predios[indice_k] + indice_k
        valores_Q[indice_k] = alturas_predios[indice_k] - indice_k

    distancia_maxima = 0 

    maior_Q_visto_ate_agora = valores_Q[0]

    for indice_j in range(1, numero_predios):
        distancia_atual = valores_P[indice_j] + maior_Q_visto_ate_agora
        
        if distancia_atual > distancia_maxima:
            distancia_maxima = distancia_atual
        
        maior_Q_visto_ate_agora = max(maior_Q_visto_ate_agora, valores_Q[indice_j])
    
    print(distancia_maxima)

if __name__ == '__main__':
    distancia_entre_amigos()