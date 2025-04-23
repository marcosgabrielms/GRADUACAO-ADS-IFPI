# Entrada 
preco = int(input('Digite o valor a receber o desconto: '))
desconto = float(input('Digite o valor do desconto aplicado: '))

# Processamenrto
valor_final = preco - (preco * desconto/100)

# Saída 
print(f'O preço final com o desconto é {valor_final}')