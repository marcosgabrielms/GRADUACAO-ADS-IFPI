# Amplie o problema de classificação de triângulos para incluir:
# Cálculo da área usando a fórmula de Heron
# Cálculo do perímetro
# Validação de possibilidade de formar um triângulo
# Classificação por lados e ângulos

from io_utils import ler_lado, exibir_resultado, exibir_mensagem_erro
import math

def formar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def classificar_por_lados(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isóceles"
    else:
        return "Escaleno"

def classificar_por_angulos (a, b, c):
    lados = sorted([a, b, c])
    x, y, z = lados
    if math.isclose(z ** 2, x ** 2 + y ** 2):
        return "Retângulo"
    elif z ** 2 > x ** 2 + y ** 2:
        return "Obtusângulo"
    else:
        return "Acutângulo"

def calcular_perimetro(a, b, c):
    return a + b + c  

def calcular_area(a, b, c):
    p = calcular_perimetro(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    print("\nClassificação de Triângulos")

    a = ler_lado("A")  
    b = ler_lado("B")  
    c = ler_lado("C")  

    if not formar_triangulo(a, b, c):
        exibir_mensagem_erro()
        return main()
    
    tipo_lados = classificar_por_lados(a, b, c)
    tipo_angulos = classificar_por_angulos (a, b, c)
    perimetro = calcular_perimetro(a, b, c)
    area = calcular_area(a, b, c)

    exibir_resultado(tipo_lados, tipo_angulos, perimetro, area)

if __name__ == "__main__":
    main()
