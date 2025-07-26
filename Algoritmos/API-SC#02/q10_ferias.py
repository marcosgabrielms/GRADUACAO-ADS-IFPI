import random

def main():

    lista_parabens = [   
    "Partiu praia! boas férias", 
    "Ouvi férias? Partiu jogar vôlei",
    "Já tá de férias!? partiu maratona de séries", 
    "Acabou as provas, vamos curtir as férias",
    "Aproveita as férias mas descansa guerreiro",
    "Parabéns, vai curtir as férias como?", 
    "Boas férias e boa viagem!", 
    "Aproveite bem as férias",
    "Agora sim vem o descanso merecido, boas férias",
    "FÉEEEERIAAAAS, AEEEEE"
    ]

    nome = input("Digite seu nome: ")

    print(f"Olá {nome}! {random.choice(lista_parabens)}")


main()