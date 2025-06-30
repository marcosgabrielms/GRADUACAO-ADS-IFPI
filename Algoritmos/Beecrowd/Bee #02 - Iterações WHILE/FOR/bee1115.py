def main():
 
  leitura_entrada = True

  while leitura_entrada:
    try:
      x, y = map(int, input().split())

      if x == 0 or y == 0:
        leitura_entrada = False
      else:
        if x > 0 and y > 0:
          print("primeiro")
        elif x < 0 and y > 0:
          print("segundo")
        elif x < 0 and y < 0:
          print("terceiro")
        elif x > 0 and y < 0:
          print("quarto")
          
    except EOFError:
      leitura_entrada = False
    except ValueError:
      leitura_entrada = False
  
if __name__ == '__main__':
 main()