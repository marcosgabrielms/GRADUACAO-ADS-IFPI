# Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
# uma mensagem de permissão de acesso ou não.

from io_utils2 import ler_inteiro, escrever

def verificar_senha():
    senha_correta = 1234
    senha_digitada = ler_inteiro("Digite a senha: ")

    if senha_digitada == senha_correta:
        escrever("Acesso permitido!")
    else:
        escrever("Senha incorreta. Acesso negado.")

def main():
    verificar_senha()

if __name__ == "__main__":
    main()
