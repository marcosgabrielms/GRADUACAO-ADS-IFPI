def main ():

   m = int(input())
   a = int(input())
   b = int(input())

   c = m - (a + b) 
   
   idade_filho_mais_velho = a

   if b > idade_filho_mais_velho:
      idade_filho_mais_velho = b
    
   if c > idade_filho_mais_velho:
      idade_filho_mais_velho = c
    
   print(idade_filho_mais_velho)


if __name__ == '__main__':
  main()