# Leia 3 números, calcule e escreva a média dos números.

def media_numeros(numero):
    n1 = numero // 100
    n2 = (numero // 10) % 10
    n3 = numero % 10
    media = (n1 + n2 + n3) / 3
    return media

# Entrada 
n = int(input("Digite um número inteiro de 03 dígitos "))

# Processamento
resultado = media_numeros(n)

# Saída
print(f"A média dos números digitados {n} é: {resultado} ")
