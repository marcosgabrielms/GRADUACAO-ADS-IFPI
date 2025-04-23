# Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

def calculo(tempo):
    semanas = tempo // (7 * 24) # Quantidade exata de semana(s) // 1 Semana = 168 horas (7 dias * 24 horas)
    resto_horas = tempo % (7 * 24) # Tempo que não formou 1 semana
    dias = resto_horas // 24 # Horas em um dia
    horas = resto_horas % 24 # horas restantes após 1 dia 
    return semanas, dias, horas

#Entrada 
tempo = int(input("Digite um número inteiro de horas: "))

# Processamento
semanas, dias, horas = calculo(tempo)

# Saída
print(f"{tempo} horas equivalem a {dias:.2f} dias, {semanas:.2f} semanas e {horas:.2f} horas")