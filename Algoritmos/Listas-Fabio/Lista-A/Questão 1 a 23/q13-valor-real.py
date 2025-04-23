# Leia um valor em real (R$), calcule e escreva 70% deste valor.

def porcentagem (numero):
    return numero * 0.70 # 70% do valor

# Entrada

valor_inicial = float(input('Digite um valor em R$: '))
print(f"70% de R$ {valor_inicial:.2f} é: R$ {porcentagem(valor_inicial):.2f}")