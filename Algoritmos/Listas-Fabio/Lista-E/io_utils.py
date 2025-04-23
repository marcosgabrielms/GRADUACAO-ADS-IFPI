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




