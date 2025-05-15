from io_q3_utils import ler_sexo, ler_nota, classificar

def main():
    total_alunos = 0
    total_homens = 0
    total_mulheres = 0

    soma_geral = 0
    soma_homens = 0
    soma_mulheres = 0

    maior_nota = float('-inf')
    menor_nota = float('inf')

    while True:
        sexo = ler_sexo()
        if sexo not in ("M", "F"):
            break
        nota = ler_nota()

        total_alunos += 1
        soma_geral += nota

        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
        
        if sexo == "M":
            total_homens += 1
            soma_homens += nota
        else:
            total_mulheres += 1
            soma_mulheres += nota
    
    media_geral = soma_geral / total_alunos if total_alunos else 0
    media_homens =  soma_homens / total_homens if total_homens else 0
    media_mulheres = soma_mulheres / total_mulheres if total_mulheres else 0

    print("\n=== RESULTADOS ===")
    print(f"Total de alunos: {total_alunos}")
    print(f"Total de homens: {total_homens}")
    print(f"Total de mulheres: {total_mulheres}")
    print(f"Maior nota geral: {maior_nota}")
    print(f"Menor nota geral: {menor_nota}")
    print(f"Média geral da turma: {media_geral:.2f} ({classificar(media_geral)})")
    print(f"Média dos homens: {media_homens:.2f} ({classificar(media_homens)})")
    print(f"Média das mulheres: {media_mulheres:.2f} ({classificar(media_mulheres)})")

if __name__ == "__main__":
    main()