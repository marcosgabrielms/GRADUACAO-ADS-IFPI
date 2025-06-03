# Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
# (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
# formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
# escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

from io_utils import ler_tres_lados, verificar_triangulo

def main():
    lado1, lado2, lado3 = ler_tres_lados()
    verificar_triangulo(lado1, lado2, lado3)

if __name__ == "__main__":
    main()
