def main():

 n = int(input("Digite o número alvo: "))

 while True:
  num = int(input("Digite um número da lista "))
  if num == n:
   print(f"Número igual ao alvo {n} encontrado. Fim da leitura.")
   break
main()