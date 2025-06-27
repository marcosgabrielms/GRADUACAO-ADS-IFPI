def main():
    
    n = int(input())

    for fator in range(1, 11):
        
        resultado = fator * n
        print(f"{fator} x {n} = {resultado}")

if __name__ == '__main__':
    main()