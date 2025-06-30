def main():
 
 senha_correta = 2002
 acesso_permitido = False

 while not acesso_permitido:
    try:
     entrada = int(input())
    except ValueError:
        continue

    if entrada == senha_correta:
      print("Acesso Permitido")
      acesso_permitido = True
    else:
      print("Senha Invalida")
  
if __name__ == '__main__':
 main()