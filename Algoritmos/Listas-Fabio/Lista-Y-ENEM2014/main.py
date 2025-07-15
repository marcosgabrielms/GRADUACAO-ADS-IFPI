import os
import consultas_enem

def exibir_menu():
    print("\n===== Software de Consulta de Dados do ENEM 2014 por Escola =====")
    print("Selecione uma consulta:")
    print("1. Ver as 'Top N' escolas por Estado (UF)")
    print("2. Calcular a Média Nacional por Área de Prova")
    print("3. Buscar uma escola por parte do nome")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_do_arquivo = os.path.join(script_dir, 'notas_por_escola_enem_2014.txt')
    
    print("Iniciando o sistema...")
    print(f"Tentando carregar dados do arquivo: '{caminho_do_arquivo}'")
    dados_enem = consultas_enem.carregar_e_normalizar_dados(caminho_do_arquivo)
    
    if dados_enem is None:
        print("Não foi possível carregar os dados. Encerrando o programa.")
        return

    opcao = -1
    while opcao != 0:
        try:
            entrada = exibir_menu()
            opcao = int(entrada)
            
            if opcao == 1:
                consultas_enem.consultar_top_n_por_uf(dados_enem)
            elif opcao == 2:
                consultas_enem.consultar_media_nacional_por_area(dados_enem)
            elif opcao == 3:
                consultas_enem.buscar_escola_por_nome(dados_enem)
            elif opcao == 0:
                print("\nEncerrando o software. Até logo!")
            else:
                print("\nOpção inválida. Por favor, tente novamente.")
        
        except ValueError:
            print(f"\nEntrada '{entrada}' inválida. Por favor, digite um número do menu.")
            opcao = -1
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            opcao = -1

if __name__ == "__main__":
    main()