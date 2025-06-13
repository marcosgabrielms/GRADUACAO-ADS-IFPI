def imprimir_com_for(n):                # Impimir a soma (1 até N) de um número N com FOR
    for i in range (1, n +1 ):
        print(i)

def imprimir_com_while(n):               # Impimir a soma (1 até N) de um número N com WHILE
    i = 1
    while i <= n:
        print(i)
        i += 1

def imprimir_com_recursao(n, atual=1):  # Impimir a soma (1 até N) de um número N com RECURSÃO
        if atual > n:
            return
        print(atual)
        imprimir_com_recursao(n, atual + 1)

def main():
     print("------------IMPRESSÃO DE 1 ATÉ N---------")
     n = int(input("Digite o valor de N:"))

     print("\nEscolha o tipo de Estrutura:")
     print("1 -> FOR")
     print("2 -> WHILE")
     print("3 -> RECURSIVIDADE")

     escolha = input("Digite o número da opção desejada: ")

     print("\nResultado: ")
     if escolha == "1":
          imprimir_com_for(n)
     elif escolha == "2":
          imprimir_com_while(n)
     elif escolha == "3":
          imprimir_com_recursao(n)
     else:
          print("Opção inválida")
main()