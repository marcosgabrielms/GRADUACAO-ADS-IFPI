def validar_nota(indice):

    nota_valida = False
    nota = 0.0

    while not nota_valida:
        try:
            nota = float(input(f"Digite a {indice + 1}ª nota: "))
            if 0.0 <= nota <= 10.0:
               nota_valida = True
            else:
                print("Nota inválida. A nota deve estar entre 0.0 e 10.0")
        except ValueError:
         print("Erro: Digite um número válido")

    return nota

def validar_pesos(indice):
    peso_valido = False
    peso = 1

    while not peso_valido:
        try:
            peso = int(input("Digite o valor do peso aplicado à nota: "))
            if 1 <= peso <= 3:
                peso_valido = True
            else: 
                print("Peso inválido. O valor do peso deve estar entre 1 e 3")
        except ValueError:
           print("Erro: Digite um número válido")
    return peso

def validar_quantidade_avaliacoes():
    avalicaoes_validas = False
    avaliacoes = 2

    while not avalicaoes_validas:
        try:
            avaliacoes = int(input("Digite o número de avaliações feitas: "))
            if 2 <= avaliacoes <= 6:
                avalicaoes_validas = True
            else:
                print("Número de avaliações inválido. A quantidade de avaliações deve ser de 2 a 6")
        except ValueError:
            print("Erro: Digite um número válido")
    return avaliacoes

def main():

    qtd_provas = validar_quantidade_avaliacoes()

    notas = []
     
    soma_ponderada = 0.0
    soma_pesos = 0

    for i in range(qtd_provas):
        nota = validar_nota(i)
        peso = validar_pesos(i)
        notas.append(nota)
        soma_ponderada += nota * peso
        soma_pesos += peso

    if len(notas) > 0:
        media_simples = sum(notas) / len(notas)
    else:
        media_simples = 0

    if soma_pesos > 0:
        media_ponderada = soma_ponderada / soma_pesos
        print(f"\nMédia ponderada: {media_ponderada:.2f}")
    else:
        print("Não foi possível calcular a média")

    print(f"\nSua nota no sistema de Média Simples: {media_simples:.2f}")

    if media_simples >= 8.0:
        print("Parabéns pelo seu desempenho!")
    
if __name__ == '__main__':
    main()