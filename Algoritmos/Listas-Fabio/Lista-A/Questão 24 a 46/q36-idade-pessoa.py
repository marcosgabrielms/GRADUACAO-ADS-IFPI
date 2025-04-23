# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

def idade_em_dias (anos, meses, dias):
    total_dias = anos * 365 + meses * 30 + dias
    return total_dias

# Entrada
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite os meses: "))
dias = int(input("Digite os dias: "))
    
# Processamento
total = idade_em_dias(anos, meses, dias)

# Saída
print(f"A idade expressa apenas em dias é: {total}")