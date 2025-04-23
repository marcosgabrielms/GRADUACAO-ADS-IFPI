# Leia o valor da base e altura de um retângulo, calcule e escreva sua área. (área = base * altura)

def area_retangulo(base,altura):
    return (base * altura) 

base = float(input("Digite o valor do base do quadrado: "))
altura = float(input("Digite o valor do altura do quadrado: "))


area = area_retangulo(base,altura)
print(f"O valor da área do quadrado é: {area:.0f}(m^2 ou cm^2) ")