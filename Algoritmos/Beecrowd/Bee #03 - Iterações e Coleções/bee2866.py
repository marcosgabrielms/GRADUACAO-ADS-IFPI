def main():

    c = int(input())

    for _ in range(c):
        palavras = str(input())
        letras_minusculas = ""
        
        for letra in palavras:
            if letra.islower():
                letras_minusculas += letra
        
        string_invertida = letras_minusculas[::-1]

        print(string_invertida)

if __name__ == '__main__':
    main()