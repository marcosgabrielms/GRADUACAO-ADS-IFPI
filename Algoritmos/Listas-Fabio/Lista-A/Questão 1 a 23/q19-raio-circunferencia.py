# Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)

def volume_esfera (pi,raio):
    return (4 * pi * raio**3) / 3 

raio = float(input("Digite o valor do raio da esfera: "))
pi = 3.14

resultado = volume_esfera (pi,raio)
print(f"O valor do volume da esfera é: {resultado:.2f}(cm^2) ")