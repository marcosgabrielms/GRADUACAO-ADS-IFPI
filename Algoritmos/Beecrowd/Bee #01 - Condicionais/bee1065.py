def main ():
    valor1 = float(input())
    valor2 = float(input())
    valor3 = float(input())
    valor4 = float(input())
    valor5 = float(input())
   
    contador_pares = 0

    if  valor1 % 2 == 0:
       contador_pares += 1
    
    if valor2 % 2 == 0:
        contador_pares += 1

    if valor3 % 2 == 0:
        contador_pares += 1

    if valor4 % 2 == 0:
        contador_pares += 1

    if valor5 % 2 == 0:
        contador_pares += 1

    print(f"{contador_pares} valores pares")

if __name__ == '__main__':
    main()