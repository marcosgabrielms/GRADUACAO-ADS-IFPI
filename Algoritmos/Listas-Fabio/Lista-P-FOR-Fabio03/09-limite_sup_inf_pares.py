def main():

 limite_inf = int(input("Digite o valor do limite inferior: "))
 limite_sup = int(input("Digite o valor do limite supeior: "))
 
 print(f"\nOs números pares entre {limite_inf} e {limite_sup} são:")

 for i in  range(limite_inf, limite_sup + 1):
  if i % 2 == 0:
   print(i)

main()