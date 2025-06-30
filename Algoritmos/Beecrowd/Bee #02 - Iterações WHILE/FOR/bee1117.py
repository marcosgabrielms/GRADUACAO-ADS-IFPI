def main():

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
            break
    
    if notas_validas == 2:
        media = (nota1 + nota2) / 2
        print(f"media = {media:.2f}")

if __name__ == '__main__':
    main()
