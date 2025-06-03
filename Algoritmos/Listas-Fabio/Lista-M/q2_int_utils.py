def main():
    # n = obter_inteiro('N: ')
    # n = obter_inteiro_while('N: ')
    # n = obter_inteiro_positivo('N: ')
    # n = obter_inteiro_minimo('N: ', 100)
    # n = obter_inteiro_maximo('N: ', 100)
    n = obter_inteiro_faixa('Digite um número entre 7 e 10: ', 7, 10)
    print(f'Valor: {n}')

def obter_inteiro(label):
    while True:
        try:
            numero = int(input(label))
            return numero
        except ValueError:
            print("Valor inválido, digite um número inteiro")
            

def obter_inteiro_while(label):
    while True:
        try:
            numero = int(input(label))
            return numero
        except ValueError:
            print("Valor inválido")     

def obter_inteiro_positivo(label):
    while True:
        numero = obter_inteiro(label)
        if numero >= 0:
            return numero
        else:
            print(f"Valor inválido, o número deve ser maior que zero")

def obter_inteiro_negativo(label):
    while True:
        numero = obter_inteiro(label)
        if numero <0:
            return numero
        else:
            print(f"Valor inválido, o número deve ser menor que zero")

def obter_inteiro_minimo(label, valor_minimo):
    while True:
        numero = obter_inteiro(label)
        if numero >= valor_minimo:
            return numero
        else:
            print(f"Valor inválido, o número deve ser maior ou igual a {valor_minimo}")

def obter_inteiro_maximo(label, valor_maximo):
    while True:
        numero = obter_inteiro(label)
        if numero <= valor_maximo:
            return numero
        else:
            print(f"Valor inválido, o número deve ser menor ou igual a {valor_maximo}")
            

def obter_inteiro_faixa(label, minimo, maximo):
    if minimo > maximo:
        print(f"O valor mínimo {minimo} não pode ser maior que o máximo {maximo}")
        return
    while True:
        numero = obter_inteiro(label)
        if minimo <= numero <= maximo:
            return numero
        else:
            print(f"Valor inválido, o número deve estar entre {minimo} e {maximo}")

if __name__ == '__main__':
    main()        