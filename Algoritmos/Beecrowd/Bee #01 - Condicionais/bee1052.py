def main():
    valor = int(input())
    lista_meses = {
        1: "January",
        2: "JFebruary",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    
    if valor in lista_meses:
        print(lista_meses[valor])

if __name__ == '__main__':
    main()
