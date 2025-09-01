def numeros_positivos(numero):
   return 1 <= numero <= 99
   
def main():
   
    primeiro_numero = None
    numero_valido = False

    while not numero_valido:
        try:
            n = int(input("Digite o primeiro número (Faixa: 1 a 99): "))
            if numeros_positivos(n):
                primeiro_numero = n
                numero_valido = True
            else:
                print("Número Inválido") 
        except ValueError:
            print("Entrada inválida, digite um número inteiro")
    
    soma = primeiro_numero
    continuar = True

    while continuar:
        try:
            n = int(input("Digite outro número (Faixa: 1 a 99): "))

            if not numeros_positivos(n):
                print("número inválido, tente novamente")
                continue 
        except ValueError:
            print("Entrada inválida, digite um número inteiro")
            continue   
             
        if n == primeiro_numero:
            soma += n
            continuar = False
        elif n % primeiro_numero == 0:
            soma += n
        
    print(f"Somatório dos múltiplos: {soma}")

main()

        
