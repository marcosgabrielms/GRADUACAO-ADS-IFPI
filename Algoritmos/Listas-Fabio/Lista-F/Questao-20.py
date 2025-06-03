# Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
# quarto) em que o ângulo se localiza.

from io_utils2 import ler_float, escrever

def identificar_quadrante(angulo):
    if 0 < angulo < 90:
        return "Primeiro quadrante"
    elif 90 < angulo < 180:
        return "Segundo quadrante"
    elif 180 < angulo < 270:
        return "Terceiro quadrante"
    elif 270 < angulo < 360:
        return "Quarto quadrante"
    elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
        return "O ângulo está sobre o eixo"
    else:
        return "Ângulo inválido"

def main():
    angulo = ler_float("Digite a medida do ângulo (entre 0° e 360°): ")

    if angulo < 0 or angulo > 360:
        escrever("Ângulo inválido! Deve ser entre 0 e 360 graus.")
        main()  
        return

    quadrante = identificar_quadrante(angulo)
    escrever(f"Localização: {quadrante}")

if __name__ == "__main__":
    main()
