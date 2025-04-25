def contar_iguais (a, b, c):

    if a == b == c:
        return "Todos os 03 números são iguais"
    elif a == b or a == c or b == c:
        return "Dois números são iguais"
    else:
        return "Nenhum número é igual"
    
def maior_e_menor(a, b):
    if a > b:
        return (a, b)
    elif b > a:
        return (b, a)
    else:
        return (a, b)  # Números iguais"
    
def maior_numero(a, b, c):      
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b  
    else:
        return c
    
        
