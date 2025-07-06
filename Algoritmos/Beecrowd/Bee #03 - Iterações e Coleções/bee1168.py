def main():

    leds_por_digito = {
        '0': 6,
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6
    }

    n = int(input())

    for _ in range(n):

        numero_str = input()

        qtd_leds = 0

        for digito in numero_str:
            qtd_leds += leds_por_digito[digito]
        
        print(f"{qtd_leds} leds")


if __name__ == '__main__':
    main()
