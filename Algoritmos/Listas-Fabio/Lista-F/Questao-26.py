# Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

from io_utils2 import ler_float, escrever

def ler_lados():
    lado1 = ler_float("Digite o primeiro lado: ")
    lado2 = ler_float("Digite o segundo lado: ")
    lado3 = ler_float("Digite o terceiro lado: ")

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        escrever("Lados devem ser positivos. Tente novamente.")
        return ler_lados()

    return lado1, lado2, lado3

def identificar_lados(lado1, lado2, lado3):
    
    if lado1 >= lado2 and lado1 >= lado3:
        hipotenusa = lado1
        cateto1 = lado2
        cateto2 = lado3
    elif lado2 >= lado1 and lado2 >= lado3:
        hipotenusa = lado2
        cateto1 = lado1
        cateto2 = lado3
    else:
        hipotenusa = lado3
        cateto1 = lado1
        cateto2 = lado2

    return hipotenusa, cateto1, cateto2

def main():
    lado1, lado2, lado3 = ler_lados()
    hipotenusa, cateto1, cateto2 = identificar_lados(lado1, lado2, lado3)

    escrever(f"Hipotenusa: {hipotenusa}")
    escrever(f"Cateto 1: {cateto1}")
    escrever(f"Cateto 2: {cateto2}")

if __name__ == "__main__":
    main()
