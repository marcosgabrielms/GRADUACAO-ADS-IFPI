# IO --> Input/Output functions
def obter_numero_real(label: str):
  return float(input(label))

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  
def obter_numero_inteiro_min(label: str, min: int):
  

  numero = obter_numero_inteiro(label)

  if numero >= min:
    return numero
  else:
    print(f'O número deve ser no mínimo {min}')
    return obter_numero_inteiro_min(label, min)
  
def numero_primo():
    try:
        num = int(input("Digite um número: "))

        if num < 2:
            print(f"O número {num} não é primo")
        else:
            eh_primo = True
            i = 2
            while i <= num // 2:
                if num % i == 0:
                    eh_primo = False
                    break
                i += 1

            if eh_primo:
                print(f"O número {num} é um número primo")
            else:
                print(f"O número {num} não é primo")

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def validar_nota(nota):
  return 0.0 <= nota <= 10.0   

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def determinar_situacao(n1, n2, n3):
   if 0.0 in (n1, n2, n3):
      return "Reprovado (nota zero)"

   media = calcular_media (n1, n2, n3)

   if media >= 7.0:
      return "Aprovado"
   elif 5.0 <= media <= 6.9:
      return "Recuperação"
   else:
      return "Reprovado"    

def calcular_desconto_base(valor):
   if valor > 500:
      return 0.15
   elif 200 <= valor <= 500:
      return 0.10
   elif 100 <= valor <= 200:
      return 0.05
   else:
      return 0.0

def calcular_desconto_adicional(vip, aniversariante):
  adicional = 0.0
  if vip:
    adicional += 0.05
  if aniversariante:
    adicional += 0.03
  return adicional     

def calcular_preco_final(valor, vip, aniversariante):
   desconto_base = calcular_desconto_base(valor)
   desconto_extra = calcular_desconto_adicional(vip, aniversariante)
   total_desconto = desconto_base + desconto_extra
   valor_final = valor * (1 - total_desconto)
   return valor_final, total_desconto

def tem_tamanho_minimo(senha):
   return len(senha) >= 8 

def tem_letra_maiuscula(senha):
    return senha.upper() != senha.lower()

def tem_letra_minuscula(senha):
   return senha.lower() != senha.upper() 

def tem_numero(senha):
   return (
      '0' in senha or
      '1' in senha or
      '2' in senha or
      '3' in senha or
      '4' in senha or
      '5' in senha or
      '6' in senha or
      '7' in senha or
      '8' in senha or
      '9' in senha 
   )

def tem_caractere_especial(senha):
   return(
      '!' in senha or
      '@' in senha or
      '#' in senha or
      '$' in senha or
      '%' in senha or
      '&' in senha or
      '*' in senha 
   )

def senha_valida(senha):
   return(
      tem_tamanho_minimo(senha) and
      tem_letra_maiuscula(senha) and
      tem_letra_minuscula(senha) and
      tem_numero(senha) and
      tem_caractere_especial(senha)
   )

def solicitar_senha():
   senha =  input("Digite uma senha: ")

   if senha_valida(senha):
      print("Senha válida! ")
      return senha
   else:
      print("\n Senha inválida. Requisitos: ")
      print(" -> Mínimo 8 caracteres")
      print(" -> Pelo menos uma letra maiúscula")
      print(" -> pelo menos uma letra minúscula")
      print(" -> pelo menos um número")
      print(" -> pelo menos um caractere especial (!@#$%&*)")
      return solicitar_senha()

def escolher_unidade():
   print("Escolha a unidade: ")   
   print("1 - Celsius")
   print("2 - Fahrenheit")
   print("3 - Kelvin")
   opcao = input()

   if opcao == "1":
      return "Celsius"
   if opcao == "2":
      return "Fahrenheit"
   if opcao == "3":
      return "Kelvin"
   else: 
       print("Opção inválida. Tente novamente.")
       return escolher_unidade()

def ler_temperatura(unidade_origem):
   print(f"Digite a temperatura em " + unidade_origem + ":")    
   entrada =  input()
   try:
      return float(entrada)
   except ValueError:
      print("Entrada inválida! Digite um número válido.")
      return ler_temperatura(unidade_origem) 

def exibir_resultado(resultado, unidade_destino):

   print(f"\nResultado: {resultado:.2f} {unidade_destino}")  

def ler_lado(nome):
   print("Digite o lado " + nome + ":")
   entrada = input()
   try:
      valor = float(entrada)
      if valor <= 0:
         print("O lado deve ser maior que zero.")
         return ler_lado(nome)
      return valor
   except ValueError:
      print("Entrada inválida! Digite um número válido")
      return ler_lado(nome)

def exibir_resultado(tipo_lados, tipo_angulos, perimetro, area):
   print("Classificação por lados: " + tipo_lados)
   print("Classificação por ângulos: " + tipo_angulos)
   print("Perímetro: " + str(round(perimetro, 2)))
   print("Área: " + str(round(area, 2)))   

def exibir_mensagem_erro():
   print("Os lados não formam um triângulo")

