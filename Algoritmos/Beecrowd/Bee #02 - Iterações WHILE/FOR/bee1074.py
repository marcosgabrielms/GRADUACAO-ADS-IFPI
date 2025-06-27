def main():

    n = int(input())

    for _ in range(n):
        x_lido = int(input())
        if x_lido == 0:
            print("NULL")
            continue
        else:
            if x_lido % 2 == 0:
                str_paridade = "EVEN"
            else:
                str_paridade = "ODD"
            
            if x_lido > 0:
                str_sinal = "POSITIVE"
            else:
                str_sinal = "NEGATIVE"

            print(f"{str_paridade} {str_sinal}")

if __name__ == '__main__':
    main()