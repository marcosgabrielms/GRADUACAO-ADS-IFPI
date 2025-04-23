# Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)

def comprimento (pi,raio):
    return (2 * pi * raio) 

raio = float(input("Digite o valor do raio da circunferência: "))
pi = 3.14


area = comprimento (pi,raio)
print(f"O valor do comprimento da circunferÇencia é: {area:.2f}(cm^2) ")