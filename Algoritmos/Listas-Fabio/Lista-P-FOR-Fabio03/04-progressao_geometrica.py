def main():

 A0 = int(input("Digite o valor de A0: "))
 limite = int(input("Digite os valores menores que o Limite: "))
 R = int(input("Digite o valor da Razão(R): "))

 termo = A0

 for _ in range(100): # "_" Usado quando não se tem o valor do índice
  if termo >= limite: # Vertifica se o termo passou da prograssão
   break
  print(termo)
  termo *= R # O próximo termo é multiplicado pela razão R


main()