def validar_idade(idade):
    return 18 <= idade <= 60
     

def validar_peso(peso):
    return peso >= 50
        
def main():
    try:
        idade = int(input("Digite a sua idade: "))
        peso = float(input("Digite o seu peso em Kg: "))
        idade_valida = validar_idade(idade)
        peso_valido = validar_peso(peso)

        print("\n--- Resultado da Avaliação ---")

        if idade_valida and peso_valido:
            print("Você está apto para doar sangue\n")
        else:
            print("Você está inapto para doar sangue, motivo(s): \n")
            if not idade_valida:
                print("-> Idade fora da faixa permitida (18 a 60 anos)")
            if not peso_valido:
                print("-> Peso inferior a 50 kg (Peso ideal)")

    except ValueError:
        print("Entrada inválida. Digite números válidos.")

main()
