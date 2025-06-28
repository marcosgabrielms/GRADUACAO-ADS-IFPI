import sys

def sequencia_secreta():
    numero_elementos = int(sys.stdin.readline())

    if numero_elementos == 0:
        print(0)
        return
    if numero_elementos == 1:
        sys.stdin.readline()
        print(1)
        return
    
    sequencia = []
    for _ in range(numero_elementos):
        sequencia.append(int(sys.stdin.readline()))

    total_marcados = 1 
    ultimo_valor_marcado_efetivamente = sequencia[0] 

    for i in range(1, numero_elementos):
        valor_atual = sequencia[i]

        if valor_atual != ultimo_valor_marcado_efetivamente:
            total_marcados += 1
            ultimo_valor_marcado_efetivamente = valor_atual
    
    print(total_marcados)

if __name__ == '__main__':
    sequencia_secreta()