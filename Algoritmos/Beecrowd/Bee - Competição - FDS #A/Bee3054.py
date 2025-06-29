def resolver():
    L, C = map(int, input().split())
    matriz = [list(map(int, input().split())) for _ in range(L)]

    if L < 2 or C < 2:
        print(0)
        return

    eh_legal_2x2 = [[False for _ in range(C - 1)] for _ in range(L - 1)]

    for r in range(L - 1):
        for c in range(C - 1):
            a11 = matriz[r][c]
            a12 = matriz[r][c + 1]
            a21 = matriz[r + 1][c]
            a22 = matriz[r + 1][c + 1]

            if a11 + a22 <= a12 + a21:
                eh_legal_2x2[r][c] = True

    maior_area = 0
    alturas = [0] * (C - 1)

    for r in range(L - 1):
        for c in range(C - 1):
            if eh_legal_2x2[r][c]:
                alturas[c] += 1
            else:
                alturas[c] = 0

        area_atual = encontrar_maior_quantidade_elementos_com_lrh(alturas)
        if area_atual > maior_area:
            maior_area = area_atual

    print(maior_area)


def encontrar_maior_quantidade_elementos_com_lrh(alturas):
    pilha = []
    max_elementos = 0
    n = len(alturas)

    for i in range(n + 1):
        altura_atual = alturas[i] if i < n else 0

        while pilha and alturas[pilha[-1]] >= altura_atual:
            topo = pilha.pop()
            altura = alturas[topo]
            largura = i if not pilha else i - pilha[-1] - 1

            # Conversão de blocos 2x2 para elementos da matriz original
            elementos = (altura + 1) * (largura + 1)

            if elementos > max_elementos:
                max_elementos = elementos

        pilha.append(i)

    return max_elementos

resolver()
