def main():

    v = int(input())

    vetores = [0] * 10
    vetores[0] = v

    for i in range(1, 10):
      
      vetores[i] = vetores[i-1] * 2  

    for i in range(10):
      
      print(f"N[{i}] = {vetores[i]}")
        

if __name__ == '__main__':
    main()        