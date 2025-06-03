# Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
# recente.

from io_utils2 import ler_inteiro, escrever

def data_maior(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return 1
    elif ano1 < ano2:
        return 2
    else:
        if mes1 > mes2:
            return 1
        elif mes1 < mes2:
            return 2
        else:
            if dia1 > dia2:
                return 1
            elif dia1 < dia2:
                return 2
            else:
                return 0  

def validar_data(dia, mes, ano):
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

def ler_data(numero):
    dia = ler_inteiro(f"Digite o dia da {numero}ª data: ")
    mes = ler_inteiro(f"Digite o mês da {numero}ª data: ")
    ano = ler_inteiro(f"Digite o ano da {numero}ª data: ")

    if not validar_data(dia, mes, ano):
        escrever("Data inválida! Tente novamente.")
        return ler_data(numero)

    return dia, mes, ano

def main():
    dia1, mes1, ano1 = ler_data(1)
    dia2, mes2, ano2 = ler_data(2)

    resultado = data_maior(dia1, mes1, ano1, dia2, mes2, ano2)

    if resultado == 1:
        escrever("A primeira data é mais recente.")
    elif resultado == 2:
        escrever("A segunda data é mais recente.")
    else:
        escrever("As duas datas são iguais.")

if __name__ == "__main__":
    main()
