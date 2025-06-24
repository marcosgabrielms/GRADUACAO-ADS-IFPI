def main():
    hora_inicio, hora_fim = map(int, input().split())
    duracao = int

    if hora_inicio < hora_fim:
        duracao = hora_fim - hora_inicio
    
    if hora_inicio > hora_fim:
        duracao = (24 - hora_inicio) + hora_fim
    
    if hora_inicio == hora_fim:
        duracao = 24

    print(f"O JOGO DUROU {duracao} HORA(S)")

if __name__ == '__main__':
    main()
