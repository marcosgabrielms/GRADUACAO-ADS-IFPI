def main():

    quantidade_divisoes = int(input())

    for _ in range(quantidade_divisoes):

        x, y = map(int, input().split())
        
        if y == 0:
            print("divisao impossivel")
        else:
            divisao_possivel = float(x) / y
            print(f"{divisao_possivel:.1f}")

if __name__ == '__main__':
    main()