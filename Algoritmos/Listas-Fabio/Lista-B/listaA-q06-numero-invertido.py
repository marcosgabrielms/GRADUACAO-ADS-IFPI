# Entrada

numero = int(input('Digite o número de três dígitos que deseja inverter: '))

# Processamento

centena = numero // 100
dezena = (numero % 100) //10
unidade = (numero % 100) % 10
inverso = (unidade * 100) + (dezena * 10) + centena


# Saída

print(f'O numero invertido é: {inverso} ')