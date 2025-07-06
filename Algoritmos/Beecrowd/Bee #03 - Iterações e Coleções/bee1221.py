def eh_primo(numero: int) -> bool:
    
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    candidato = 3
    while candidato * candidato <= numero:
        if numero % candidato == 0:
            return False
        candidato += 2
        
    return True

def main():
    qtd = int(input())

    while qtd > 0:
        numero = int(input())

        if eh_primo(numero):
            print("Prime")
        else:
            print("Not Prime")
        
        qtd -= 1

if __name__ == '__main__':
    main()