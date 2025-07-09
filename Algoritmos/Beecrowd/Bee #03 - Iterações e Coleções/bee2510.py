def main():

   
    vilao_capturado = lambda vilao: True

    t = int(input())

    for _ in range(t):
        
        vilao_encontrado = input()

        if vilao_capturado(vilao_encontrado):
            print("Y")
        else:
            print("N")

if __name__ == '__main__':
    main()