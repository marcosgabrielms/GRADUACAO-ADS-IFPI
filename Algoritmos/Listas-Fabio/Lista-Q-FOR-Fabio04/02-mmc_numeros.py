def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    candidato =  max(n1, n2) 

    while True:
        if candidato %  n1 == 0 and candidato % n2 == 0:
            print(f"O MMC de {n1} e {n2} é: {candidato}") 
            break
        candidato +=1
main()