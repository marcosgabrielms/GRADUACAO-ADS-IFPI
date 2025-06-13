def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
def main():
    print("\n------Cálculo do Número Fatorial-------")
    n = int(input("Digite o valor do número (n): "))
    resultado = fatorial(n)
    print(f"O fatorial de {n} é {resultado}")
    print("FIM")

main()