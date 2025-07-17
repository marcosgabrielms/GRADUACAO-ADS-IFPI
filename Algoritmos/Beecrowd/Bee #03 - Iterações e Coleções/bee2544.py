import sys
import math

for linha in sys.stdin:
    n = int(linha)
    
    if n == 1:
        print(0)
    else:
        resultado = int(math.log2(n))
        print(resultado)