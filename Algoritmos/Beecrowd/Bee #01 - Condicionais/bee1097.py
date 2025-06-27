def main():
    
    i = 1
    j_inicial = 7

    while i <= 9:
        j = j_inicial

        while j >= (j_inicial - 2):

            print(f"I={i} J={j}")

            j -= 1
            
        i += 2
        j_inicial += 2
    

if __name__ == '__main__':
   main()
