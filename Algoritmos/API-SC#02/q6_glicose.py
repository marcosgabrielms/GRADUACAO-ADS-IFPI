def clasificar_glicose(glicose):

    if glicose < 100:
        return "Categoria: Normal"
    elif 100 <= glicose < 126:
        return "Categoria: Pré-diabetes"
    else:
        return "Categoria: Diabetes"

def main():
    try:
        valor_glicose = float(input("Digite o valor da glicose (mg/dL): "))
        categoria = clasificar_glicose(valor_glicose)
        print(f"Classificação: {categoria}")
    except ValueError:
        print("Por favor, digite um número válido")

main()