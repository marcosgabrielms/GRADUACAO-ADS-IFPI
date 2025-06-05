def main():

 while True:
  numero = int(input("\nDigite um número ou pressione 0 para sair: "))

  if numero == 0:
    break #Flag
  
  print(f"\nNúmero: {numero}")
  print("Divisores:", end=" ") # O end pega o print para terminar com um espaço vazio ao invés de pular a linha

  for i in range(1, numero + 1):
    if numero % i == 0:
     print(i, end=" ")

 print("\n")

main()