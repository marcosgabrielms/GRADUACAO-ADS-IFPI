def main():

    n = int(input())

    ho = ''

    for i in range(n):
    
        if i + 1 == n:
            ho += 'Ho!'

        else:
            ho += 'Ho '
       
    print(ho) 
    
if __name__ == '__main__':
    main()