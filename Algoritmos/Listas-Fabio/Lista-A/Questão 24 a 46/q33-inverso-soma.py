# Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
def calculo_numero(n):
    n1 = n // 100
    n2 = (n // 10) % 10
    n3 = n  % 10
    numero_invertido = n3 * 100 + n2 * 10 + n1
    diferenca =  abs (n + numero_invertido)
    return diferenca

# Entrada
n = int(input("Digite um número inteiro de 03 dígitos: "))

# Processamento

conta = calculo_numero(n)

# Saída

print(f"O calculo do número digitado e seu inverso é: {conta}")