def gerar_primos(qtd):
    primos = []
    candidato = 2
    while len(primos) < qtd:
        if eh_primo(candidato):
            primos.append(candidato)
        candidato += 1
    return primos

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def josephus_primo(n):
    pessoas = list(range(1, n + 1))
    primos = gerar_primos(n)
    indice = 0

    for i in range(n - 1):
        m = primos[i]
        indice = (indice + m - 1) % len(pessoas)
        pessoas.pop(indice)

    return pessoas[0]

def main():
    while True: 
        n = int(input()) 

        if n == 0: 
            break 
        else:
           
            print(josephus_primo(n))

if __name__ == "__main__":
    main()