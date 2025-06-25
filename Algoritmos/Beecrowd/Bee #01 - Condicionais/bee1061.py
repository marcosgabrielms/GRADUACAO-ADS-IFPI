def calcular_duracao(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio, dia_fim, hora_fim, minuto_fim, segundo_fim):

    segundos_por_minuto = 60
    segundos_por_hora = 60 * segundos_por_minuto
    segundos_por_dia = 24 * segundos_por_hora

    total_segundos_inicio = (dia_inicio * segundos_por_dia) + \
                            (hora_inicio * segundos_por_hora) + \
                            (minuto_inicio * segundos_por_minuto) +\
                            segundo_inicio
    total_segundos_fim = (dia_fim * segundos_por_dia) + \
                         (hora_fim * segundos_por_hora) + \
                         (minuto_fim* segundos_por_minuto) + \
                         segundo_fim

    duracao_segundos = total_segundos_fim - total_segundos_inicio

    if duracao_segundos < 0:
        duracao_segundos += segundos_por_dia
    
    dias = duracao_segundos // segundos_por_dia
    segundos_restantes = duracao_segundos % segundos_por_dia

    horas = segundos_restantes // segundos_por_hora
    segundos_restantes %= segundos_por_hora

    minutos =  segundos_restantes // segundos_por_minuto

    segundos = segundos_restantes % segundos_por_minuto

    return dias, horas, minutos, segundos


def main():

    data_inicio = input().split()
    horario_inicio = input().split(':')
    data_fim = input().split()
    horario_fim = input().split(':')
    
    dia_inicio = int(data_inicio[1]) 
    hora_inicio = int(horario_inicio[0])
    minuto_inicio = int(horario_inicio[1])
    segundo_inicio = int(horario_inicio[2])

    dia_fim = int(data_fim[1])
    hora_fim = int(horario_fim[0])
    minuto_fim = int(horario_fim[1])
    segundo_fim = int(horario_fim[2])

    dias_duracao, horas_duracao, minutos_duracao, segundos_duracao = calcular_duracao(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio, dia_fim, hora_fim, minuto_fim, segundo_fim)

    print(f"{dias_duracao} dia(s)")
    print(f"{horas_duracao} hora(s)")
    print(f"{minutos_duracao} minuto(s)")
    print(f"{segundos_duracao} segundo(s)")



if __name__ == '__main__':
    main()