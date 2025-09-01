def main():

    qtd_nomes_digitados = 0
    nome = input("\nDigite um nome ou digite 'fim' para encerrar: ").strip()

    while nome.lower() != "fim":
        if len(nome) > 4:
            qtd_nomes_digitados += 1
        else:
            print("Nome com menos de 4 caracteres serão ignorados")
        
        nome = input("\nDigite outro nome ou digite 'fim' para encerrar: ")

    print(f"\nQuantidade de nomes digitados (com mais de 4 letras): {qtd_nomes_digitados} nomes")
    
main()

            