# Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
# hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
# máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
# seguinte.

from io_utils2 import ler_inteiro, escrever

def calcular_duracao(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
    inicio_em_minutos = hora_inicio * 60 + minuto_inicio
    fim_em_minutos = hora_fim * 60 + minuto_fim

    if fim_em_minutos < inicio_em_minutos:
        fim_em_minutos += 24 * 60  # jogo terminou no dia seguinte

    duracao_total = fim_em_minutos - inicio_em_minutos
    horas = duracao_total // 60
    minutos = duracao_total % 60

    return horas, minutos

def main():
    hora_inicio = ler_inteiro("Digite a hora de início (0-23): ")
    minuto_inicio = ler_inteiro("Digite o minuto de início (0-59): ")
    hora_fim = ler_inteiro("Digite a hora de fim (0-23): ")
    minuto_fim = ler_inteiro("Digite o minuto de fim (0-59): ")

    if not (0 <= hora_inicio <= 23 and 0 <= minuto_inicio <= 59 and 0 <= hora_fim <= 23 and 0 <= minuto_fim <= 59):
        escrever("Hora ou minuto inválido! Tente novamente.")
        main()  
        return

    horas, minutos = calcular_duracao(hora_inicio, minuto_inicio, hora_fim, minuto_fim)

    escrever(f"Duração do jogo: {horas} hora(s) e {minutos} minuto(s)")

if __name__ == "__main__":
    main()
