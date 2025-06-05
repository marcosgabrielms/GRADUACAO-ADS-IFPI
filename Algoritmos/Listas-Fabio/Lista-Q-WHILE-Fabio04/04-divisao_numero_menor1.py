def main():

 numero = int(input("Digite um número: "))
 resultados = []

 while numero > 1:
    resultados.append(numero)
    numero = numero // 2

 for i in range(len(resultados)):
   if i == len(resultados) - 1:
     print(f"{resultados[i]}")
   else:
     print(f"{resultados[i]} ÷ 2 -> ", end="")




 print(f"O último resultado maior ou igual a 1 foi: {resultados[-1]}")

 

main()