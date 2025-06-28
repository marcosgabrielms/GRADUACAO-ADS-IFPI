def parcelamento_sem_juros():

    valor = int(input())
    parcela = int(input())

    parcela_base = valor // parcela

    resto = valor % parcela

    if resto == 0:
        for _ in range(parcela):
         print(parcela_base)
    else:
        for _ in range(resto):
            print(parcela_base + 1)
        
        for _ in range(parcela - resto):
            print(parcela_base)

if __name__ == '__main__':
    parcelamento_sem_juros()    