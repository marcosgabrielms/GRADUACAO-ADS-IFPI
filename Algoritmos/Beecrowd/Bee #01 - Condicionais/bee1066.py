def main ():
    valor1 = float(input())
    valor2 = float(input())
    valor3 = float(input())
    valor4 = float(input())
    valor5 = float(input())
   
    contador_pares = 0
    contador_impar = 0
    contador_positivos = 0
    contador_negativos = 0

    if valor1 % 2 == 0:
       contador_pares += 1
    else:
       contador_impar += 1
    
    if valor1 > 0:
        contador_positivos += 1
    elif valor1 < 0:
        contador_negativos += 1

    if valor2 % 2 == 0:
        contador_pares += 1
    else:
        contador_impar += 1

    if valor2 > 0:
        contador_positivos += 1
    elif valor2 < 0:
        contador_negativos += 1    
    
    if valor3 % 2 == 0:
        contador_pares += 1
    else:
        contador_impar += 1
    if valor3 > 0:
        contador_positivos += 1
    elif valor3 < 0:
        contador_negativos += 1

    if valor4 % 2 == 0:
        contador_pares += 1
    else:
        contador_impar += 1
    
    if valor4 > 0:
        contador_positivos += 1
    elif valor4 < 0:
        contador_negativos += 1
    
    if valor5 % 2 == 0:
        contador_pares += 1
    else:
        contador_impar += 1
    if valor5 > 0:
        contador_positivos += 1
    elif valor5 < 0:
        contador_negativos =+ 1

    print(f"{contador_pares} valor(es) par(es)")
    print(f"{contador_impar} valor(es) impar(es)")
    print(f"{contador_positivos} valor(es) positivo(s)")
    print(f"{contador_negativos} valor(es) negativo(s)")

if __name__ == '__main__':
    main()