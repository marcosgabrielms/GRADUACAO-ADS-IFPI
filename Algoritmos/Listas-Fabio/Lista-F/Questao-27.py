# Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
# nascimento e a data (dia, mês e ano) atual.

from io_utils2 import ler_inteiro, escrever

def ler_data(tipo):
    dia = ler_inteiro(f"Digite o dia da {tipo}: ")
    mes = ler_inteiro(f"Digite o mês da {tipo}: ")
    ano = ler_inteiro(f"Digite o ano da {tipo}: ")

    if not data_valida(dia, mes, ano):
        escrever("Data inválida! Tente novamente.")
        return ler_data(tipo)

    return dia, mes, ano

def data_valida(dia, mes, ano):
    if ano <= 0 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):  
            return dia <= 29
        else:
            return dia <= 28
    return True

def calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual):
    anos = ano_atual - ano_nasc
    meses = mes_atual - mes_nasc
    dias = dia_atual - dia_nasc

    if dias < 0:
        meses -= 1
        dias += 30  

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

def main():
    dia_nasc, mes_nasc, ano_nasc = ler_data("nascimento")
    dia_atual, mes_atual, ano_atual = ler_data("data atual")

    anos, meses, dias = calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual)

    escrever(f"Idade: {anos} anos, {meses} meses e {dias} dias.")

if __name__ == "__main__":
    main()
