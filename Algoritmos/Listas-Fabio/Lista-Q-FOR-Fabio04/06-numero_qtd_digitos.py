def main():

 numero = int(input("Digite um número: "))
 numero_inicial = abs(numero) # Salva o valor absoluto do número e usa no cálculo, mantendo o número original

 qtd_digitos = 0

 while numero_inicial > 0:
  numero_inicial = numero_inicial // 10
  qtd_digitos += 1 # Incrementa o contador de dígitos
  qtd_digitos = qtd_digitos or 1
 
 
 print(f"O número {abs(numero)} tem: {qtd_digitos} dígito(s)")


main()