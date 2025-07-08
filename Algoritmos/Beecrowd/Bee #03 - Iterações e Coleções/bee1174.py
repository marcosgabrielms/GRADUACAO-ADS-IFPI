def main():

    entrada_vetores = [0] * 100

    for i in range(100):
      
     entrada_vetores[i] = float(input())

    for i in range(100):
       if entrada_vetores[i] <= 10:
          print(f"A[{i}] = {entrada_vetores[i]:.1f}")


if __name__ == '__main__':
    main()        