# Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior ou igual a cada uma das duas prestações; estas devem ser iguais,
# inteiras e as maiores possíveis. Por exemplo, se o valor da mercadoria for R$ 270,00, a entrada e as duas prestações são iguais a R$ 90,00; se o valor da
# mercadoria for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações são iguais a R$ 100,00. Escreva um algoritmo que receba o valor da mercadoria e forneça
# o valor da entrada e das duas prestações, de acordo com as regras acima.

def calcular_pagamento(valor):
    prestacao = valor // 3
    entrada = valor - 2 * prestacao
    return entrada, prestacao

# Entrada
valor_total = int(input("Digite o valor da mercadoria: "))

# Processamento
entrada, prestacao = calcular_pagamento(valor_total)

# Saída
print(f"Entrada: R${entrada}")
print(f"2 prestações de R${prestacao}")
