def contar_iguais (a, b, c):

    if a == b == c:
        return "Todos os 03 números são iguais"
    elif a == b or a == c or b == c:
        return "Dois números são iguais"
    else:
        return "Nenhum número é igual"
    
def maior_e_menor(a, b):
    if a > b:
        return (a, b)
    elif b > a:
        return (b, a)
    else:
        return (a, b)  # Números iguais"
    
def maior_numero(a, b, c):      
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b  
    else:
        return c

def ler_numero():
     try:
         num = int(input("Digite um número de dois dígitos (10 a 99): "))
         if 10 <= num <= 99:
             return num
         else:
             print("Número inválido! Deve ser entre 10 a 99.")
             return ler_numero()
     except ValueError:
         print("Entrada inválida! Digite apenas números inteiros")
         return ler_numero()
def verificar_digitos(num):
    dezena =  num // 10
    unidade = num % 10

    if dezena == unidade:
        print("O algarismo de dezena é igual ao algarismo da unidade")
    else:
        print("O algarismo da dezena é diferente do algarismo da unidade")         

def ler_numero():
    while True:
        try:
            num = int(input("Digite um número de dois dígitos (10 a 99): "))
            if 10 <= num <= 99:
                return num
            else:
                print("Número inválido! Deve ser entre 10 e 99.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

def verificar_digitos(num):
    dezena = num // 10
    unidade = num % 10

    if dezena == unidade:
        print("O algarismo da dezena é IGUAL ao algarismo da unidade.")
    else:
        print("O algarismo da dezena é DIFERENTE do algarismo da unidade.")


def ordenar_numeros(a, b, c):
    if a <= b <= c:
        print("números em ordem crescente: ", a, b, c)
    else:
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a

        return ordenar_numeros(a, b, c)                    

def ler_angulo(mensagem):
    try:
        angulo = int(input(mensagem))
        if 0 < angulo < 180:
            return angulo
        else:
            print("Ângulo inválido! Deve ser maior que 0 e menor que 180.")
            return ler_angulo(mensagem)  
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        return ler_angulo(mensagem)  

def verificar_triangulo(a, b, c):
    
    soma = a + b + c

    if soma == 180:
        print(f"Os ângulos {a}°, {b}° e {c}° formam um triângulo.")

       
        if a < 90 and b < 90 and c < 90:
            print("É um triângulo Acutângulo (todos os ângulos menores que 90°).")
        elif a == 90 or b == 90 or c == 90:
            print("É um triângulo Retângulo (um ângulo igual a 90°).")
        elif a > 90 or b > 90 or c > 90:
            print("É um triângulo Obtusângulo (um ângulo maior que 90°).")
    else:
        print(f"Os ângulos {a}°, {b}° e {c}° NÃO formam um triângulo.")

def ler_lado(mensagem):
    try:
        lado = int(input(mensagem))
        if lado > 0:
            return lado
        else:
            print("Lado inválido! Deve ser maior que 0.")
            return ler_lado(mensagem)  # Chamar a si mesma (recursão)
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        return ler_lado(mensagem)  # Chamar a si mesma (recursão)

def ler_tres_lados():
    lado1 = ler_lado("Digite o primeiro lado: ")
    lado2 = ler_lado("Digite o segundo lado: ")
    lado3 = ler_lado("Digite o terceiro lado: ")
    return lado1, lado2, lado3

def verificar_triangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print(f"Os lados {a}, {b} e {c} formam um triângulo.")
        classificar_triangulo(a, b, c)
    else:
        print(f"Os lados {a}, {b} e {c} NÃO formam um triângulo.")

def classificar_triangulo(a, b, c):
    if a == b == c:
        print("É um triângulo Equilátero (todos os lados iguais).")
    elif a == b or b == c or a == c:
        print("É um triângulo Isósceles (dois lados iguais).")
    else:
        print("É um triângulo Escaleno (todos os lados diferentes).")

def ler_data(mensagem):
    try:
        data_str = input(mensagem)
        
        # Ler diretamente como inteiros sem usar split
        dia = int(data_str[0:2])
        mes = int(data_str[3:5])
        ano = int(data_str[6:10])

        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:
            return dia, mes, ano
        else:
            print("Data inválida! Verifique os valores e digite novamente.")
            return None  # Retorna None caso os valores sejam inválidos
    except (ValueError, IndexError):
        print("Formato inválido! Use o formato DD/MM/AAAA.")
        return None  # Retorna None se o formato não for correto

def calcular_idade(dia_nascimento, mes_nascimento, ano_nascimento, dia_atual, mes_atual, ano_atual):
    idade = ano_atual - ano_nascimento
    
    # Verifica se a pessoa já fez aniversário este ano
    if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
        idade -= 1  # Se não fez aniversário ainda neste ano
    return idade

def ler_numero(mensagem):
    try:
        numero_str = input(mensagem)
        
        # Ler diretamente o número e verificar se está no intervalo 0-100
        numero = int(numero_str)
        
        if 0 <= numero <= 100:
            return numero
        else:
            print("Número fora do intervalo! Digite um número entre 0 e 100.")
            return None
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
        return None

def verificar_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    for i in range(2, int(numero ** 0.5) + 1):  # Verificação até a raiz quadrada do número
        if numero % i == 0:
            return False  # Se for divisível por qualquer número, não é primo
    return True  # Se passar em todas as verificações, é primo

def ler_data(mensagem):
    try:
        data_str = input(mensagem)
        
        
        dia = int(data_str[0:2])
        mes = int(data_str[3:5])
        ano = int(data_str[6:10])

        if 1 <= mes <= 12 and 1 <= dia <= 31 and ano > 0:
          
            if mes == 2:  
                if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) and dia > 29:
                    print("Data inválida! Fevereiro tem 29 dias no ano bissexto.")
                    return None
                if dia > 28:  
                    print("Data inválida! Fevereiro tem no máximo 28 dias (ou 29 em ano bissexto).")
                    return None
            elif mes in [4, 6, 9, 11] and dia > 30:  
                print("Data inválida! O mês selecionado tem no máximo 30 dias.")
                return None
            elif mes not in [4, 6, 9, 11] and dia > 31:  
                print("Data inválida! O mês selecionado tem no máximo 31 dias.")
                return None
            return dia, mes, ano
        else:
            print("Data inválida! O mês deve estar entre 1 e 12, e o dia dentro do intervalo correto.")
            return None
    except (ValueError, IndexError):
        print("Formato inválido! Use o formato DD/MM/AAAA.")
        return None

def ler_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        return ler_inteiro(mensagem)

def escrever(mensagem):
    print(mensagem)

def ler_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        return ler_inteiro(mensagem)

def escrever(mensagem):
    print(mensagem)

def ler_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        return ler_inteiro(mensagem)

def escrever(mensagem):
    print(mensagem)

def ler_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        return ler_inteiro(mensagem)

def ler_float(mensagem):
    try:
        return float(input(mensagem))
    except ValueError:
        return ler_float(mensagem)

def escrever(mensagem):
    print(mensagem)

def ler_float(mensagem):
    try:
        return float(input(mensagem))
    except ValueError:
        return ler_float(mensagem)

def escrever(mensagem):
    print(mensagem)


        
