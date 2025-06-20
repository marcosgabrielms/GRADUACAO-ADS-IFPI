def main():
    n1, n2, n3, n4 = map(float, input().split())

    media_inicial = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

    print(f"Media: {media_inicial:.1f}")

    if media_inicial >= 7.0:
        print("Aluno aprovado")
    if media_inicial < 5.0:
        print("Aluno reprovado")
    else:
        print("Aluno em exame")

        nota_exame = float(input())
        print(f"Nota do exame: {nota_exame:.1f}")

        media_final = (media_inicial + nota_exame) / 2

        if media_final >= 5.0:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")
        
        print(f"Media final: {media_final:.1f}")

if __name__ == '__main__':
    main()