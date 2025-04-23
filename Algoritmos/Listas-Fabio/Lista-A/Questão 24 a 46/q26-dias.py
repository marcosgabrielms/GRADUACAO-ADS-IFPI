# Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

def dias_para_semanas (dias):
    semanas = dias // 7
    dias_restantes = dias % 7
    return semanas, dias_restantes

# Entrada 
dias = float(input("Digite o número de dias: "))

# Processamento
semanas, dias_restantes = dias_para_semanas(dias)

# Saída
print(f"{dias} dias equivalem a {semanas} semana(s) e {dias_restantes} dias(s)")