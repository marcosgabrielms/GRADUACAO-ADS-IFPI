def main():
    a, b, c = map(float, input().split())

    valores_originais = [a, b, c]
    valores_ordenados = [a, b, c]

    if valores_ordenados[0] > valores_ordenados[1]:
        valores_ordenados[0], valores_ordenados[1] = valores_ordenados[1], valores_ordenados[0]
    
    if valores_ordenados[1] > valores_ordenados[2]: 
        valores_ordenados[1], valores_ordenados[2] = valores_ordenados[2], valores_ordenados[1]
    
    if valores_ordenados[0] > valores_ordenados[1]:
        valores_ordenados[0], valores_ordenados[1] = valores_ordenados[1], valores_ordenados[0]

    print(f"{valores_ordenados[0]:.0f}")
    print(f"{valores_ordenados[1]:.0f}")
    print(f"{valores_ordenados[2]:.0f}")

    print()

    print(f"{valores_originais[0]:.0f}")
    print(f"{valores_originais[1]:.0f}")
    print(f"{valores_originais[2]:.0f}")

if __name__ == '__main__':
    main()