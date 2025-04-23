# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
#distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor
#seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e
#escreva o custo ao consumidor.

def custo_carro_novo(custo_fabrica, porcentagem_dist, imposto):
    distribuidor = custo_fabrica * (porcentagem_dist / 100)
    imposto = custo_fabrica * (imposto / 100)
    custo_total = custo_fabrica + distribuidor +imposto 
    return custo_total

# Entrada
custo_fabrica = float(input('Digite o custo de fábrica do carro:'))

# Processamento
custo_final = custo_carro_novo(custo_fabrica, 28, 45)

# Saída

print(f"O custo do carro novo será de R$ {custo_final:.2f}")