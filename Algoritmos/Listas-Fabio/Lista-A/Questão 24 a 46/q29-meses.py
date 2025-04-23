# Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.
def calculo_meses(meses):
    anos = meses // 12
    meses_restantes = meses % 12
    return anos, meses_restantes
    
# Entrada 
meses = float(input("Digite um número inteiro de meses "))

# Processamento]
anos, meses_restantes = calculo_meses(meses)

# Saída
print(f"{meses} meses equivalem a {anos} anos e {meses_restantes} meses")