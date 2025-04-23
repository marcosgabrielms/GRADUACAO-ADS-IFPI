# Um sistema de equações lineares do tipo ax + by = c; dx + ey = f, pode ser resolvido segundo mostrado abaixo

def sistema_linear(a, b, c, d, e, f):
    delta = a * e - b * d
    x = (c * e - b * f) / delta
    y = (a * f - c * d) / delta
    return x, y

# Entrada
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))

# Processamento

x,y = sistema_linear(a, b, c, d, e, f)

# Saída
print(f"Solução do sistema:\nx = {x:.2f}\ny = {y:.2f}")



