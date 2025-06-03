# Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
# se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
# verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
# obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

import io_utils

def main():
    ang1 = io_utils.ler_angulo("Digite o primeiro ângulo: ")
    ang2 = io_utils.ler_angulo("Digite o segundo ângulo: ")
    ang3 = io_utils.ler_angulo("Digite o terceiro ângulo: ")
    
    io_utils.verificar_triangulo(ang1, ang2, ang3)

if __name__ == "__main__":
    main()

