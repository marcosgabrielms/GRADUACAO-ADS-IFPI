def main():

    vetor_par = [0] * 5
    vetor_impar = [0] * 5
    contador_par = 0
    contador_impar = 0

    for _ in range(15):

        numero_lido = int(input())

        if numero_lido % 2 == 0:
            vetor_par[contador_par] = numero_lido
            contador_par += 1
            if contador_par == 5:
                for i in range(5):
                    print(f"par[{i}] = {vetor_par[i]}")
                contador_par = 0
        else:
            vetor_impar[contador_impar] = numero_lido
            contador_impar += 1
            if contador_impar == 5:
                for i in range(5):
                    print(f"impar[{i}] = {vetor_impar[i]}")
                contador_impar = 0

    for i in range(contador_impar):
        print(f"impar[{i}] = {vetor_impar[i]}")

    for i in range(contador_par):
        print(f"par[{i}] = {vetor_par[i]}")

if __name__ == '__main__':
    main()