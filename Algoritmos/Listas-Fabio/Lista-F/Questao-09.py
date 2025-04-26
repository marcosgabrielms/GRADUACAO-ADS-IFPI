# Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

from io_utils import ler_numero, verificar_primo

def ler_numero_valido(mensagem):
    numero = ler_numero(mensagem)
    if numero is None:  # Se a entrada for inválida, chama a função novamente
        return ler_numero_valido(mensagem)
    return numero

def main():
    # Lê o número e garante que ele esteja no intervalo 0-100
    numero = ler_numero_valido("Digite um número entre 0 e 100: ")
    
    # Verifica se o número é primo
    if verificar_primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")

if __name__ == "__main__":
    main()
