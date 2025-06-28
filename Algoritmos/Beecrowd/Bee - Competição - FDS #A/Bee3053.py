import sys

def jogo_dos_copos():
    N = int(sys.stdin.readline())
    
    pos_atual_moeda = sys.stdin.readline().strip()

    for _ in range(N):
        tipo_movimento = int(sys.stdin.readline())

        if tipo_movimento == 1:
            if pos_atual_moeda == 'A':
                pos_atual_moeda = 'B'
            elif pos_atual_moeda == 'B':
                pos_atual_moeda = 'A'
        elif tipo_movimento == 2:
            if pos_atual_moeda == 'B':
                pos_atual_moeda = 'C'
            elif pos_atual_moeda == 'C':
                pos_atual_moeda = 'B'
        elif tipo_movimento == 3:
            if pos_atual_moeda == 'A':
                pos_atual_moeda = 'C'
            elif pos_atual_moeda == 'C':
                pos_atual_moeda = 'A'
    
    print(pos_atual_moeda)

if __name__ == '__main__':
    jogo_dos_copos()