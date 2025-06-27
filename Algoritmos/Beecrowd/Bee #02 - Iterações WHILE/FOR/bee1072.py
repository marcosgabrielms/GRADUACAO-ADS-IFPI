def main():
    n = int(input())
    
    contador_dentro_intervalo = 0
    contador_fora_intervalo = 0

    for _ in range(n):
        x_lido = int(input())
        
        if x_lido >= 10 and x_lido <= 20:
            contador_dentro_intervalo += 1
        else: 
            contador_fora_intervalo += 1
    print(f"{contador_dentro_intervalo} in")
    print(f"{contador_fora_intervalo} out")

if __name__ == '__main__':
    main()
