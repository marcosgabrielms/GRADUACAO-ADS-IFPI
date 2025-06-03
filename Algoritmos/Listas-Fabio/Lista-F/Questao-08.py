# Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
# sua idade exata (em anos).

from io_utils import ler_data, calcular_idade

def ler_data_valida(mensagem):
    data = ler_data(mensagem)
    if data is None:  # Se a data for inválida, chama a função novamente
        return ler_data_valida(mensagem)
    return data

def main():
    # Lê a data atual e a data de nascimento, garantindo que ambas as entradas sejam válidas
    dia_atual, mes_atual, ano_atual = ler_data_valida("Digite a data atual (DD/MM/AAAA): ")
    dia_nascimento, mes_nascimento, ano_nascimento = ler_data_valida("Digite sua data de nascimento (DD/MM/AAAA): ")

    idade = calcular_idade(dia_nascimento, mes_nascimento, ano_nascimento, dia_atual, mes_atual, ano_atual)
    print(f"Sua idade exata é {idade} anos.")

if __name__ == "__main__":
    main()
