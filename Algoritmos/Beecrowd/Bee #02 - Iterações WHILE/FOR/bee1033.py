import sys

def calcular_periodo_pisano(modulo_do_calculo):
    if modulo_do_calculo == 1:
        return 1
    
    modulo_fib_anterior = 0
    modulo_fib_atual = 1

    comprimento_periodo = 0

    for _ in range(modulo_do_calculo * modulo_do_calculo + 2):

        modulo_proximo_fib = (modulo_fib_anterior + modulo_fib_atual) % modulo_do_calculo
        modulo_fib_anterior = modulo_fib_atual
        modulo_fib_atual = modulo_proximo_fib

        comprimento_periodo += 1

        if modulo_fib_anterior == 0 and modulo_fib_atual == 1:
            break

    return comprimento_periodo

def calcular_modulo_fibonaci(indice_fib, modulo_do_calculo):

    if indice_fib == 0:
        return 0
    if indice_fib == 1:
        return 1
    
    valor_fib_anterior = 0
    valor_fib_atual = 1

    for _ in range(2, indice_fib + 1):
        valor_proximo_fib = (valor_fib_anterior + valor_fib_atual) % modulo_do_calculo
        valor_fib_anterior = valor_fib_atual
        valor_fib_atual = valor_proximo_fib

    return valor_fib_atual

def main():

    numero_do_caso = 1

    linha_de_entrada = sys.stdin.readline().strip()

    while linha_de_entrada != "0 0":

        valor_n_entrada, modulo_base_b = map(int, linha_de_entrada.split())
        print(f"Case {numero_do_caso}: {valor_n_entrada} {modulo_base_b}", end=" ")

        if modulo_base_b == 1:
            print(0)
            numero_do_caso += 1
            linha_de_entrada = sys.stdin.readline.strip()
            continue

        periodo_pisnano = calcular_periodo_pisano(modulo_base_b)
        
        indice_reduzido_efetivo = (valor_n_entrada + 1) % periodo_pisnano

        valor_fib_indice_efetivo = calcular_modulo_fibonaci(indice_reduzido_efetivo, modulo_base_b)
        
        ultimo_digito_resultado = (2 * valor_fib_indice_efetivo - 1 ) % modulo_base_b

        print(ultimo_digito_resultado)

        numero_do_caso += 1
        linha_de_entrada = sys.stdin.readline().strip()

if __name__ == '__main__':
    main()