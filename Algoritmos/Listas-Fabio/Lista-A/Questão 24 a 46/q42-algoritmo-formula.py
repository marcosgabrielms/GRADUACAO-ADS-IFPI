# Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e
# ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.

def distancia (x1, y1, x2, y2):
    plano1 = (x2 - x1) ** 2
    plano2 = (y2 - y1) ** 2
    d = (plano1 + plano2) ** 0.5
    return d

# Entrada
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

# Processamento

dist =  distancia(x1, y1, x2, y2)

# Saída

print(f"A distância entre os pontos no plano é: {dist:.2f}")