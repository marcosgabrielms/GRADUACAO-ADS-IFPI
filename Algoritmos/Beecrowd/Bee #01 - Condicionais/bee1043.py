def eh_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def main ():
    a, b, c = map(float, input().split())
    if eh_triangulo(a, b, c):
        perimetro = a + b + c
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((a + b) * c) / 2
        print(f"Area = {area:.1f}")

if __name__ == '__main__':
    main()
            