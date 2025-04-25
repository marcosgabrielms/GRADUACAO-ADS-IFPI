# Desenvolva um programa que verifique se uma senha atende aos seguintes
# critérios de segurança:
# Pelo menos 8 caracteres
# Pelo menos uma letra maiúscula
# Pelo menos uma letra minúscula
# Pelo menos um número
# Pelo menos um caractere especial (!, @, #, $, %, &, *)

from io_utils import solicitar_senha

def main():
    print("Validador de Senhas")
    senha = solicitar_senha()
    print(f"Sua senha '{senha}' foi registrada com sucesso.")

if __name__ == "__main__":
    main()