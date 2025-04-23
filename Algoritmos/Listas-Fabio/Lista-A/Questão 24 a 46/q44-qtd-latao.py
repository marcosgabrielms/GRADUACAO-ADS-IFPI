# Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a
# quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada
# pelo usuário.

def calcular_latao(qtd_latao):
    cobre = qtd_latao * 0.70
    zinco = qtd_latao * 0.30
    return cobre, zinco

# Entrada
qtd_latao = float(input("Digite a quantidade de latão (em kg): "))

# Processamento
cobre, zinco = calcular_latao(qtd_latao)

# Saída
print(f"Para {qtd_latao:.2f} kg de latão, você precisa de:")
print(f"{cobre:.2f} kg de cobre")
print(f"{zinco:.2f} kg de zinco")
