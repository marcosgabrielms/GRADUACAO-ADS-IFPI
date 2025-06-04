def main():

 A0 = int(input("Digite o valor de A0: "))
 limite = int(input("Digite os valores menores que o Limite: "))
 R = int(input("Digite o valor da Razão(R): "))

 for termo in range(A0, limite, R):
  print(termo)

main()