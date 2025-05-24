def ler_sexo():
    sexo = input("Digite o sexo do aluno (M/F) ou qualquer outra tecla para sair: ").strip().upper()
    return sexo

def ler_nota():
    while True:
        try:
            nota_str = input("Digite a nota do aluno (1 a 10): ").replace(",", ".")
            nota = float(nota_str)
            if 1 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite um valor entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 10.")

def classificar(media):
    if 0 <= media <= 2:
        return "Péssimo"
    elif 2 < media <= 4:
        return "Ruim"
    elif 4 < media <= 7:
        return "Regular"
    elif 7 < media <= 8:
        return "Bom"
    elif 8 < media <= 10:
        return "Excelente"
    else:
        return "Inválido"
