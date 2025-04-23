# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

def dias_para_idade(total_dias):
    anos = total_dias // 365
    resto = total_dias % 365
    meses = resto // 30
    dias = resto % 30
    return anos, meses, dias

# Entrada
total_dias = int(input("Digite a idade expressa apenas em dias: "))

# Processamento
anos, meses, dias = dias_para_idade(total_dias)

# Saída
print(f"A idade é: {anos} anos, {meses} meses e {dias} dias")
