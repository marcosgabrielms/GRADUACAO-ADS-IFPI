# Entrada 
capital = float(input('Digite o valor do Capital Inicial(Reais): '))
taxa = float(input('Digite o valor do Taxa de Juros(%): '))
tempo = float(input('Digite o valor do Tempo de Aplicação(meses): '))

# Processamento

juros = capital * taxa * tempo
montante = float(capital + juros)

# Saída

print(f'O valor do Montante Final da aplicação é {montante}')
