# Funções para o import da questão 1 (q1) #
def eh_valido(novo, anterior):   #Verifica se um dígito é válido comparado ao anterior
    if novo == anterior:
        return False
    if novo == anterior + 1:
        return False
    if novo == anterior - 1:
        return False 
    return True

def gerar_digito(semente): # Semente ou Seed é um valor inicial base para gerar uma sequência  de números
    return (semente * 7 + 3) % 10

def gerar_senha_rec(n, contador, senha="", anterior=None): # Gera senha usando recursão, montando um número de n dígitos
    if len(senha) == n:
        return senha,contador
    
    pessoa = gerar_digito(contador)
    if anterior is None or eh_valido(pessoa, anterior): # Se ainda não tem o anterior (primeiro dígito) o ou novo dígito for válido
        return gerar_senha_rec(n, contador + 1, senha + str(pessoa), pessoa)
    else:
        return gerar_senha_rec(n, contador + 1, senha, anterior)
    
def ler_tamanho_senha():
    while True:
        try:
            n = int(input("Digite o tamanho da senha (quantidade de dígitos): "))
            if n > 0:
                return n
            else:
                print("Digite um número maior que 0.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro")

def perguntar_satisfacao():
    resposta =  input("Está satisfeito com a senha? (s/n): ").strip().lower()
    return resposta == "s"

# Funções para o import da questão 2 (q2) #

# ===== ENTRADA COM VALIDAÇÃO ==== #
def ler_sexo(masculino, feminino):
    while True:
        try:
            if ler_sexo == masculino and feminino:
                return ler_sexo
        except ValueError:
            print("Informação inválida, digite apenas se você é do sexo masculino o feminino!")

def ler_inteiro_positivo(mensagem):
    while True:
        entrada =  input(mensagem)
        if entrada.isdigit():
            valor = int(entrada)
            if valor > 0:
                return valor
            print("Valor inválido. Digite um número maior que zero")

def ler_percentual_transport():
    while True:
        entrada = input("Digite a porcentagem de tempo para o Transport: ")
        if entrada.isdigit():
            percentual = int(entrada)
            if 0 <= percentual <= 100:
                return percentual
            print("Valor inválido. Digite um número entre 0 e 100.")        

def ler_sexo():
    while True:
        entrada = input("Digite o seu sexo (homem ou mulher): ").strip().lower()
        if entrada == "homem" or entrada == "mulher":
            return entrada
        print("Valor inválido. Digite apenas 'homem' ou 'mulher.")

# ==== CÁLCULOS ==== #
def calorias_por_minutos(sexo, exercicio):
    if exercicio == "transport":
        if sexo == "homem":
            return 100 / 5
        else: # Mulher
            return 100 / 6
    elif exercicio == "escada":
        if sexo == "homem":
            return 100 / 7
        else: # Mulher
            return 100 / 8

def distribuir_tempo(minutos_dia, percentual_transport):
    minutos_transport = int(minutos_dia * percentual_transport / 100)
    minutos_escada = minutos_dia - minutos_transport
    return minutos_transport, minutos_escada

def gasto_semanal(min_escada, min_transport, cal_escada, cal_transport, dias_semana):
    calorias_dia = (min_escada * cal_escada) + (min_transport * cal_transport)
    calorias_semana = calorias_dia * dias_semana
    return calorias_semana

import math

def semanas_necessarias(quilos, calorias_semana):
    total_calorias = quilos * 7000
    semanas =  total_calorias / calorias_semana
    return math.ceil(semanas)
