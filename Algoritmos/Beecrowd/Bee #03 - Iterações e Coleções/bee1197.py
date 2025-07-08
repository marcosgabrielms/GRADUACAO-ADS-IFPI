import sys

def main():

    for linha in sys.stdin:

        v, t = map(int, linha.split())

        deslocamento = v * t * 2
        print(deslocamento)


if __name__ == '__main__':
    main()
