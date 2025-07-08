def main():

    vetor = [0] * 20

    for i in range(20):
        vetor[i] = int(input())

    for i in range(10):
        j = 19 - i

        vetor[i], vetor[j] = vetor[j], vetor[i] 
    
    for i in range(20):
        
        print(f"N[{i}] = {vetor[i]}")
    
if __name__ == '__main__':
    main()