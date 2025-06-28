import sys

def nota_cortada():
    largura_nota = 160
    altura_nota = 70
    area_total_nota = largura_nota * altura_nota

    area_minima_nota = area_total_nota / 2

    b = int(sys.stdin.readline())
    t = int(sys.stdin.readline())

    area_felix = ((b + t) / 2) * altura_nota
    area_marzia = area_total_nota - area_felix

    felix_nota = False
    marzia_nota = False

    if area_felix > area_minima_nota and area_marzia <= area_minima_nota:
        felix_nota = True
    if area_marzia > area_minima_nota and area_felix <= area_minima_nota:
        marzia_nota = True

    if felix_nota:
        print(1)
    elif marzia_nota:
        print(2)
    else:
        print(0)

if __name__ == '__main__':
    nota_cortada()