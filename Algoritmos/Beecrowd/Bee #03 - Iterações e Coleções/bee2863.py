import sys

linhas = iter(sys.stdin)

for linha_t in linhas:
    t = int(linha_t)
    tempos = [float(next(linhas)) for _ in range(t)]
    print(min(tempos))