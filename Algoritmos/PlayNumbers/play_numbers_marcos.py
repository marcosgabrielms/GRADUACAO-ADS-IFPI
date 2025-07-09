import operacoes_vetor as op
from io_utils import pressione_enter_para_continuar

def mostrar_menu():
    print("\n" + "="*30)
    print("        PLAY NUMBERS ")
    print("="*30)
    print(" 1. Inicializar Vetor")
    print(" 2. Mostrar todos os valores")
    print(" 3. Resetar Vetor")
    print(" 4. Ver quantidade de itens no vetor")
    print(" 5. Ver Menor e Maior valores")
    print(" 6. Somatório dos Valores")
    print(" 7. Média dos Valores")
    print(" 8. Mostrar Valores Positivos")
    print(" 9. Mostrar Valores Negativos")
    print("10. Atualizar todos os valores")
    print("11. Adicionar Novo Valor")
    print("12. Remover Itens por Valor")
    print("13. Remover por Posição")
    print("14. Editar valor por Posição")
    print("15. Salvar valores em arquivo")
    print("16. Ordenar Vetor")
    print("17. Embaralhar Vetor")
    print("18. Sair")
    print("="*30)

def main():
    vetor_principal = []
    opcao = ''

    menu_opcoes = {
        '1': op.executar_inicializacao,
        '2': op.mostrar_todos,
        '3': op.resetar_vetor,
        '4': op.ver_quantidade,
        '5': op.ver_maior_menor,
        '6': op.ver_somatorio,
        '7': op.ver_media,
        '8': op.ver_positivos,
        '9': op.ver_negativos,
        '10': op.executar_atualizacao,
        '11': op.adicionar_novo_valor,
        '12': op.remover_por_valor,
        '13': op.remover_por_posicao,
        '14': op.editar_por_posicao,
        '15': op.salvar_em_arquivo,
        '16': op.ordenar_vetor,
        '17': op.embaralhar_vetor
    }

    while opcao != '18':
        mostrar_menu()
        opcao = input(">> Escolha uma opção: ")

        if opcao == '18':
            if vetor_principal:
                salvar = input("Deseja salvar as alterações em um arquivo antes de sair? (s/n): ").lower()
                if salvar == 's':
                    op.salvar_em_arquivo(vetor_principal)
            print("Saindo da aplicação...")
            break
        
        funcao_selecionada = menu_opcoes.get(opcao)

        if funcao_selecionada:
            vetor_principal = funcao_selecionada(vetor_principal)
        else:
            print("Opção inválida! Por favor, tente novamente.")
        
        pressione_enter_para_continuar()

if __name__ == "__main__":
    main()