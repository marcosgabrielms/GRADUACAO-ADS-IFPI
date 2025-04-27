# Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
# um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
# não pode ser negativo.

from io_utils2 import ler_float, escrever

def ler_ponto(numero_ponto):
    x = ler_float(f"Digite a coordenada x do ponto {numero_ponto}: ")
    y = ler_float(f"Digite a coordenada y do ponto {numero_ponto}: ")
    return x, y

def calcular_area(x1, y1, x2, y2):
    base = abs(x2 - x1)
    altura = abs(y2 - y1)
    return base * altura

def main():
    x1, y1 = ler_ponto(1)
    x2, y2 = ler_ponto(2)

    area = calcular_area(x1, y1, x2, y2)

    escrever(f"A área do retângulo é: {area}")

if __name__ == "__main__":
    main()
