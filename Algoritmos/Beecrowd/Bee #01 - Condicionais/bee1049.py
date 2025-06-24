def main():
    palavra1 = str(input())
    palavra2 = str(input())
    palavra3 = str(input())

    if palavra1 == "vertebrado":
        if palavra2 == "ave":
            if palavra3 == "carnivoro":
                print("aguia")
            else:
                print("pomba")
        else:
            if palavra3 == "herbivoro":
                print("vaca")
            else:
                print("homem")
    else:
        if palavra2 == "inseto":
            if palavra3 == "herbivoro":
                print("lagarta")
            else:
                print("pulga")
        else:
            if palavra3 == "onivoro":
                print("minhoca")
            else:
                print("sanguessuga")

if __name__ == '__main__':
    main()
