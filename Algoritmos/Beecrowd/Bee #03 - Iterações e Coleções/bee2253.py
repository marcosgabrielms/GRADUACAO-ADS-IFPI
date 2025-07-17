import sys

def validar_senha(senha):

    if not(6 <= len(senha) <= 32):
        return False
    
    tem_minuscula = False
    tem_maiuscula = False
    tem_numero = False

    for char in senha:
        if 'a' <= char <= 'z':
            tem_minuscula = True
        elif 'A' <= char <= 'Z':
            tem_maiuscula = True
        elif '0' <= char <= '9':
            tem_numero = True
        else:
            return False
        
    if tem_minuscula and tem_maiuscula and tem_numero:
        return True
    else:
        return False
    
for linha in sys.stdin:

    senha = linha.strip()

    if validar_senha(senha):
        print("Senha valida.")
    else:
        print("Senha invalida.")