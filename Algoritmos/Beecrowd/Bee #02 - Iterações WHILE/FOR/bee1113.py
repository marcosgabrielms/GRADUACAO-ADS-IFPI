def main():
    x = 0
    y = 1

    while x != y:

        x, y = map(int, input().split())

        if x > y:
            print("Decrescente")
        elif x < y:
            print("Crescente")
        
        
if __name__ == '__main__':
    main()

