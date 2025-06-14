def main():
    ...

    qtd_dias =  int(input("Digite a quantidade de dias para análise: "))
    limite_calorico = int(input("Digite o limite de calorias por dia: "))
    soma_total_calorias = 0
    maior_consumo_dia = 0
    menor_consumo_dia = 0
    dia_maior_consumo = 0
    dia_menor_consumo = 0


    for  dia_atual in range(1, qtd_dias + 1):
        print(f"\n----DIA {dia_atual}----")

        cal_cafe = int(input("Qtd de calorias do café da manhã: "))
        cal_almoco = int(input("Qtd de calorias do café do almoço: "))
        cal_jantar = int(input("Qtd de calorias do jantar: "))
        cal_lanches = int(input("Qtd de calorias dos lanches: "))
      
        total_calorias_dia = cal_cafe + cal_almoco + cal_jantar + cal_lanches
        print(f"O total de calorias do dia {dia_atual} é: {total_calorias_dia}")

        soma_total_calorias += total_calorias_dia

        if dia_atual == 1:
            maior_consumo_dia = total_calorias_dia
            menor_consumo_dia = total_calorias_dia
            dia_maior_consumo = 1
            dia_menor_consumo = 1
        else:
            
            if total_calorias_dia > maior_consumo_dia:
                maior_consumo_dia = total_calorias_dia
                dia_maior_consumo = dia_atual

            if total_calorias_dia < menor_consumo_dia:
                menor_consumo_dia = total_calorias_dia
                dia_menor_consumo =  dia_atual

        media_diaria = soma_total_calorias / qtd_dias

        print(f"\n-----Resultado Final------")
        print(f"A média do consumo diário foi de {media_diaria:.2f} calorias.")
        print(f"O dia de maior consumo foi o dia {dia_maior_consumo}, com {maior_consumo_dia} calorias")
        print(f"O dia de menor consumo foi o dia {dia_menor_consumo}, com {menor_consumo_dia} calorias")

        if media_diaria > limite_calorico:
            print(f"Atenção! Sua média de {media_diaria:.2f} calorias excedeu o seu limite de {limite_calorico} calorias")
        else:
            print(f"Parabéns! sua média de {media_diaria:.2f} calorias está dentro do seu limite de {limite_calorico} calorias")

main ()