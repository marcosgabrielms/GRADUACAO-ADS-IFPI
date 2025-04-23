# Leia um valor em m, calcule e escreva o equivalente em cm.
def m_to_cm (valor):
    return valor * 100

# Entrada 
m = float(input("Digite o valor em metros:  "))

# Processamento

cm = m_to_cm (m)

# Saída

print(f"{m} metros equivalem a  {cm:.2f} centímetros")
