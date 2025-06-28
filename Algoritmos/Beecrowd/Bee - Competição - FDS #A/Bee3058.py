def supermercado():

    n = int(input())

    primeiro_mercado = input().split()
    p_primeiro = float(primeiro_mercado[0])
    g_primeiro = int(primeiro_mercado[1])

    menor_preço_por_kg = (p_primeiro / g_primeiro) * 1000

    for _ in range(n - 1):
        entrada = input().split()

        p = float(entrada[0])
        g = int(entrada[1])

        preço_por_kg_atual = (p / g) * 1000

        if preço_por_kg_atual < menor_preço_por_kg:
            menor_preço_por_kg = preço_por_kg_atual

    print(f"{menor_preço_por_kg:.2f}")

if __name__ == '__main__':
    supermercado()