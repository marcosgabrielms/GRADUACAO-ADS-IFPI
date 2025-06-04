def main ():

 n = int(input("Digite um número: "))
 limiteinf = int(input("Digite o valor do limite inferior: "))
 limitesup = int(input("Digite o valor do limite superior: "))

 print(f"\nMúltiplos de {n} entre {limiteinf} e {limitesup} são:")
 for i in range(limiteinf, limitesup + 1):
  resultado = n * i
  print(f"{n} x {i} = {resultado}")

main()