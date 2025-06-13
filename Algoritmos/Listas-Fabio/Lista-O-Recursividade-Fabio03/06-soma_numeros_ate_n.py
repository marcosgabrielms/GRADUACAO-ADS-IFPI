def somar_ate_n(n):
    if n <= 1:
        return 1
    else:
        return n + somar_ate_n(n - 1)

def main():
    print("\n-----Somar até N--------")
    n = int(input("Digite o valor do número (n): "))
    resultado = somar_ate_n(n)
    print(f"A soma de 1 até {n} é: {resultado}")
    print("FIM")
main()