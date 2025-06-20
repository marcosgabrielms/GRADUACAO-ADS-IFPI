import math

def main():
    a = float(0.0)
    b = float(20.0)
    c = float(5.0)


    delta = b**2 - 4 * a * c

    if a == 0.0 or delta < 0:
        print("Impossivel Calcular")
    else:
        raiz_delta = math.sqrt(delta)
        R1 = (-b + raiz_delta) / (2 * a)
        R2 = (-b - raiz_delta) / (2 * a)

        print(f"R1 =  {R1:.5f}")
        print(f"R2 =  {R2:.5f}")

if __name__ == '__main__':
    main()
    