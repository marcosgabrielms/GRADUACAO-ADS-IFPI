# Desenvolva um programa que receba três notas de um aluno, calcule a média e
# determine sua situação com base nos critérios:
# Média >= 7.0: Aprovado
# Média entre 5.0 e 6.9: Recuperação
# Média < 5.0: Reprovado

from io_utils import validar_nota, calcular_media, determinar_situacao

def main():
    try:
        n1 = float(input("Digite a 1º nota: "))
        n2 = float(input("Digite a 2º nota: "))
        n3 = float(input("Digite a 3º nota: "))

        if not validar_nota(n1):
            print("Erro: A 1º nota deve estar entre 0 e 10.")    
            return
        if not validar_nota(n2):
            print("Erro: A 2º nota deve estrar entre 0 e 10.")
            return
        if not validar_nota(n3):
            print("Erro: A 3º nota deve estrar entre 0 e 10.")
            return
        
        media = calcular_media(n1, n2, n3)
        situacao = determinar_situacao(n1, n2, n3)

        print(f"\nMédia: {media:.2f}")
        print(f"Situação: {situacao}")

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")

if __name__ == "__main__":
    main()