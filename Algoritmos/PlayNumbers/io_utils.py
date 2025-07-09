def obter_numero(mensagem='Digite um número: ', tipo=float):
        try:
            valor = tipo(input(mensagem))

            return ValueError
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            return obter_numero(mensagem, tipo)

def pressione_enter_para_continuar():
    input("\nPressione Enter para continuar...")