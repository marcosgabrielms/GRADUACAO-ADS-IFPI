alimentos = {
    "arroz": {"calorias": 130, "proteinas": 2.7},
    "feijao": {"calorias": 135, "proteinas": 8.5},
    "frango": {"calorias": 165, "proteinas": 31},
    "bife": {"calorias": 250, "proteinas": 27},
    "ovo": {"calorias": 155, "proteinas": 13},
    "pão": {"calorias": 265, "proteinas": 9},
    "queijo": {"calorias": 402, "proteinas": 25},
    "banana": {"calorias": 89, "proteinas": 1.1},
    "maça": {"calorias": 52, "proteinas": 0.3},
    "alface": {"calorias": 15, "proteinas": 1.4}
}

qtd_pessoas =  int(input("Digite a quantidade de pessoas: "))
maior_consumo_calorico =  0
pessoa_do_maior_consumo = 0
menor_consumo_calorico = 0
pessoa_menor_consumo = 0

for pessoa in range(1, qtd_pessoas +1):
    print(f"\n----DADOS DA PESSOA {pessoa} ----")
    total_calorias_pessoa = 0
    total_proteinas_pessoa = 0
    qtd_alimentos = int(input(f"Quantos alimentos para a pessoa {pessoa} ?: "))
    
    print(f"Opções de Alimentos: ", end="")
    for nome in alimentos.keys():
        print(nome, end=" ")
    print()
    
    for i in range(qtd_alimentos):
        print(f"\n--Alimento {i + 1} de {qtd_alimentos} --")

        while True:
            nome_alimento =  input("Digite o nome do alimento: ").lower()
            if nome_alimento in alimentos:
                break
            else:
                print("Alimento inválido! Digite um alimento da lista.")

        gramas = int(input(f"Digite a quantidade de '{nome_alimento}' em gramas:"))

        calorias_calculadas = (alimentos[nome_alimento]["calorias"] / 100) * gramas
        proteinas_calculadas = (alimentos[nome_alimento]["proteinas"] / 100) * gramas

        total_calorias_pessoa += calorias_calculadas
        total_proteinas_pessoa += proteinas_calculadas

        print(f"+ {calorias_calculadas}:.0f calorias e {proteinas_calculadas:.1f}g de proteínasn adicionadas" )
        print(f"\n--- RESUMO PARA A PESSOA {pessoa} ---")
        print(f"Total de calorias consumidas: {total_calorias_pessoa:.0f} cal")
        print(f"Total de proteínas consumidas: {total_proteinas_pessoa:.1f} g")

        if pessoa == 1:
            maior_consumo_calorico = total_calorias_pessoa
            menor_consumo_calorico = total_calorias_pessoa
            pessoa_do_maior_consumo = pessoa
            pessoa_menor_consumo = pessoa
        else:
            if total_calorias_pessoa > maior_consumo_calorico:
                maior_consumo_calorico = total_calorias_pessoa
                pessoa_do_maior_consumo = pessoa
            
            if total_calorias_pessoa < menor_consumo_calorico:
                menor_consumo_calorico = total_calorias_pessoa
                pessoa_menor_consumo = pessoa
    print("\n--- DESTAQUES GERAIS ---")
    print(f"Pessoa com MAIOR consumo de calorias: Pessoa {pessoa_do_maior_consumo} ({maior_consumo_calorico:.0f} cal)")
    print(f"Pessoa com MENOR consumo de calorias: Pessoa {pessoa_menor_consumo} ({menor_consumo_calorico:.0f} cal)")
        
   
