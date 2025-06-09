def imprimir_pares(n):
    if n == 0:
        return
    imprimir_pares(n - 1)
    if n % 2 == 0:
        print(n)

print("Digite um número inteiro positivo maior que 1: ")
n = int(input())

print(f" Números pares de 1 até {n}")
imprimir_pares(n)