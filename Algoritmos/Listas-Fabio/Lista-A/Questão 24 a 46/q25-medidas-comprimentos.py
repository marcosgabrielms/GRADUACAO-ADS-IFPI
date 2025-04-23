# Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

def medida_comprimento(valor):
    return valor / 1000

# Entrada
m = float(input("Digite um valor inteiro de metros: "))

# Processamento

km = medida_comprimento(m)

# Saída

print(f"O valor digitado corresponde a {m} metros que equivalem a {km} quilômetros")