# Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
# ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
# final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
# escreva “Reprovado”.

from io_utils import ler_float, escrever

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        exame = ler_float("Digite a nota do exame: ")
        media_final = (media + exame) / 2
        if media_final >= 5.0:
            return "Aprovado"
        else:
            return "Reprovado"

def main():
    nota1 = ler_float("Digite a primeira nota: ")
    nota2 = ler_float("Digite a segunda nota: ")

    media = calcular_media(nota1, nota2)
    resultado = verificar_aprovacao(media)

    escrever(resultado)

if __name__ == "__main__":
    main()
