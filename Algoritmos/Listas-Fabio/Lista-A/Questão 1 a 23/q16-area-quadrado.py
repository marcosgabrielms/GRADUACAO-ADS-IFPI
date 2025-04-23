# Leia o valor do lado de um quadrado, calcule e escreva sua área. (área = lado^2)

def area_quadrado(lado):
    return (lado**2) 

lado = float(input("Digite o valor do lado do quadrado: "))


area = area_quadrado(lado)
print(f"O valor da área do quadrado é: {area:.0f}(m^2 ou cm^2) ")