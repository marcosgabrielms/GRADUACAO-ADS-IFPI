def main():

    n = int(input())

    for n_teste in range(1, 10001):
        
        if n_teste % n == 2:
            
            print(n_teste)

if __name__ == '__main__':
    main()