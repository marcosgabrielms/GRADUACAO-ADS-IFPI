import math
def main():
    h1, m1, h2, m2 = map(int, input().split())

    duracao_min = (((h2 * 60) + m2) - ((h1 * 60) + m1))
    hora = 0
    minuto = 0

    if duracao_min <= 0:
        duracao_min += 1440
    hora = math.floor(duracao_min / 60) 
    minuto = duracao_min % 60
        
    print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")

if __name__ == '__main__':
    main()
