# Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

def dinheiro_gasto (anos, cigarros_dias, preco_carteira):
    total_cigarros = anos * 365 * cigarros_dias
    total_gasto = (total_cigarros / 20) * preco_carteira
    return total_gasto

# Entrada
qtd_cigarros = int(input("Digite a quantidade de cigarros que você fuma por dia: "))
qtd_anos =  int(input("Digite o tempo em anos que você fuma: "))
preco_carteira = float(input("Digite o preço de uma carteira de cigarros: "))

# Processamento

gasto_total = dinheiro_gasto(qtd_anos, qtd_cigarros, preco_carteira)

# Saída
print(f"Você já gastou R$ {gasto_total:.2f} com cigarros, se cuida irmão e pare de fumar")