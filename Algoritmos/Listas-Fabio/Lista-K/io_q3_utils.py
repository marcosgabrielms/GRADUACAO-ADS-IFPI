def ler_sexo():
    while True:
        sexo = input("Digite o sexo do aluno (M/F): ").strip().upper()
        if sexo in ("M", "F"):
            return sexo
        else:
            print("Sexo inválido. Digite M para Masculino ou F para feminino")

def ler_nota():
    while True:
        try:
            nota = float(input("Digite a nota do aluno (1 a 10): ").replace(",", "."))
            if 1 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite um valor entre 1 e 10.")
        except ValueError:
                print("Entrada inválida. Digite um número entre 1 e 10.")

def classificar(media):
    if 0 <= media <= 2:
        return "Péssimmo"
    elif 2 <= media <= 4:
        return "Ruim"
    elif 4 <= media <= 7:
        return "Regular"
    elif 7 <= media <= 8:
        return "Bom"
    elif 8 <= media <= 10:
        return "Excelente"
    else:
        return "Inválido"