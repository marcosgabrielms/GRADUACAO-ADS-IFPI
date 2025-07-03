import sys

for line in sys.stdin:
    try:
        numeros_str = line.strip().split()
        num1 = int(numeros_str[0])
        num2 = int(numeros_str[1])
                
        resultado = num1 ^ num2
        
        print(resultado)
    except ValueError:
        continue
    except IndexError:
        continue