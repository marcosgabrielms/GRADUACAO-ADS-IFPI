def main ():
    x, y = map(float, input().split())

    if x == 0 and (y > 0 or y < 0):
        print("Eixo Y")
    elif y == 0 and (x > 0 or x < 0):
        print("Eixo X")
    elif x > 0:
        if y > 0:
            print("Q1")
        elif y < 0:
            print("Q4")
    elif x < 0:
        if y > 0:
            print("Q2")
        elif y < 0:
            print("Q3")
    else:
        print("Origem")

main()