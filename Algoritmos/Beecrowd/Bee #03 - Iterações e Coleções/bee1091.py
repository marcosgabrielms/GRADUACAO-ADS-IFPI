import sys

def main():
    
    k = int(sys.stdin.readline().strip())
    
    while k != 0:
        n, m = map(int, sys.stdin.readline().strip().split())
        
        for _ in range(k):
            x, y = map(int, sys.stdin.readline().strip().split())

            if x == n or y == m:
                print("divisa")
            elif x > n and y > m:
                print("NE")
            elif x < n and y > m:
                print("NO")
            elif x < n and y < m:
                print("SO")
            else:
                print("SE")

        k = int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()