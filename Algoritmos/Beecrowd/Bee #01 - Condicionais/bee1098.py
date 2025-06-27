def main():
    i = 0.0
    j_inicial = 1.0 
    epsilon = 1e-9

    while i <= 2.0 + epsilon:
        j = j_inicial

        while j <= (j_inicial + 2.0 + epsilon):
            if abs(i - round(i)) < epsilon:
                i_formatado = int(round(i))
            else:
                i_formatado = f"{i:.1f}"

            if abs(j - round(j)) < epsilon:
                j_formatado = int(round(j))
            else:
                j_formatado = f"{j:.1f}"
            
            print(f"I={i_formatado} J={j_formatado}")

            j += 1.0
            
        i += 0.2
        j_inicial += 0.2
    
if __name__ == '__main__':
    main()