def main():

    executar_novo_calculo = True

    while executar_novo_calculo:
        nota1 = -1.0
        nota2 = -1.0
        notas_validas = 0

        while notas_validas < 2:
            try:
                nota = float(input())

                if 0 <= nota <= 10:
                    if notas_validas == 0:
                        nota1 = nota
                    else:
                        nota2 = nota
                    
                    notas_validas += 1
                else:
                    print("nota invalida")
            except ValueError:
                print("nota invalida")
            except EOFError:
                return
    
        if notas_validas == 2:
            media = (nota1 + nota2) / 2
            print(f"media = {media:.2f}")

        opcao_valida = False
        
        while not opcao_valida:
            print("novo calculo (1-sim 2-nao)")
            try:
                opcao = int(input())
                if opcao == 1 or opcao == 2:
                    opcao_valida = True
            except ValueError:
                continue
            except EOFError:
                return

        if opcao == 2:
            executar_novo_calculo = False


if __name__ == '__main__':
    main()
