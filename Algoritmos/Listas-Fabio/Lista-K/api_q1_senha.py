from io_utils import gerar_senha_rec, ler_tamanho_senha, perguntar_satisfacao

def main():
    print("Gerador de senha segura")
    n = ler_tamanho_senha()
    contador = 1

    while True:
        senha, contador =  gerar_senha_rec(n, contador)
        print("\nSenha sugerida: ", senha)
        if perguntar_satisfacao():
            print("\nSenha aceita!")
            break

if __name__ == "__main__":
    main()        