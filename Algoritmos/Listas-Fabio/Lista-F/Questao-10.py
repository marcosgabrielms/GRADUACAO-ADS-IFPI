# Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

from io_utils import ler_data

def ler_data_valida(mensagem):
    data = ler_data(mensagem)
    if data is None:  
        return ler_data_valida(mensagem)
    return data

def main():
    
    dia, mes, ano = ler_data_valida("Digite uma data (DD/MM/AAAA): ")

    print(f"A data {dia}/{mes}/{ano} é válida.")

if __name__ == "__main__":
    main()
