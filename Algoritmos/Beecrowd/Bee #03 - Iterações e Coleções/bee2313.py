lados = list(map(int, input().split()))

lados.sort()

a, b, c = lados[0], lados[1], lados[2]

if a + b > c:
    tipo_triangulo = ""
    if a == b and b == c:
        tipo_triangulo = "Equilatero"
    elif a != b and b != c and a != c:
        tipo_triangulo = "Escaleno"
    else:
        tipo_triangulo = "Isoceles"

    print(f"Valido-{tipo_triangulo}")

    if a**2 + b**2 == c**2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")