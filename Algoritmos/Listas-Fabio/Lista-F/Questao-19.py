# Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
# (IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso (IMC entre 25 e 30) 
# ou obesidade mórbida (IMC acima de 30).

from io_utils2 import ler_float, escrever

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def classificar_imc(imc):
    if imc < 25:
        return "Peso normal"
    elif imc <= 30:
        return "Obeso"
    else:
        return "Obesidade mórbida"

def main():
    altura = ler_float("Digite a altura em metros: ")
    peso = ler_float("Digite o peso em kg: ")

    if altura <= 0:
        escrever("Altura inválida! Deve ser maior que 0.")
        main()  
        return

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    escrever(f"IMC: {imc:.2f}")
    escrever(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()
