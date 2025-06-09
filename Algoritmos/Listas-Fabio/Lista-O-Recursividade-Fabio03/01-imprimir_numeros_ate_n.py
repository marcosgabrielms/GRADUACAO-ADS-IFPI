def somar_entradas_recursivo(soma_parcial=0):
    try:
        entrada_str = input(f"Digite um número para somar (Soma atual: {soma_parcial}). Digite 0 para parar: ")
        numero = int(entrada_str)

        if numero == 0:
            print("--- Fim da recursão ---")
            return soma_parcial

        return somar_entradas_recursivo(soma_parcial + numero)

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
        return somar_entradas_recursivo(soma_parcial)


print("Iniciando a soma recursiva...")
soma_total = somar_entradas_recursivo()

print(f"\nA SOMA TOTAL FOI: {soma_total}")