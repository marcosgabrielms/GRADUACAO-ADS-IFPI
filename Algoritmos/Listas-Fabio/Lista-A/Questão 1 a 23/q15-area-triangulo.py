# Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)

def area_triangulo(base,altura):
    return (base * altura) / 2

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area = area_triangulo(base,altura)
print(f"O valor da área do triângulo é: {area:.0f} cm^2 ")