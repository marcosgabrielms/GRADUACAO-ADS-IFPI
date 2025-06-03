# Crie um programa para uma loja que calcule o preço final de um produto com base
# em regras de desconto:
# Compras acima de R$ 500,00: 15% de desconto
# Compras entre R$ 200,00 e R$ 500,00: 10% de desconto
# Compras entre R$ 100,00 e R$ 199,99: 5% de desconto
# Cliente VIP: desconto adicional de 5% (acumulativo)
# Cliente Aniversariante: desconto adicional de 3% (acumulativo)

from io_utils import calcular_preco_final

def main ():
    try:
        valor = float(input("Digite o valor da compra: R$ "))
        vip_input = input("Cliente VIP? (s/n): ")
        aniversario_input = input("É aniversário do cliente? (s/n): ")

        vip = vip_input == 's' or vip_input == 'S'
        aniversariante =  aniversario_input == 's' or aniversario_input == 'S',

        preco_final, total_desconto = calcular_preco_final(valor, vip, aniversariante)

        print(f"\nDesconto total aplicado: {total_desconto * 100:.1f} %")
        print(f"Preço final:R$ {preco_final:.2f}")

    except ValueError:
        print("Erro: Digite um valor válido para a compra")

if __name__ == "__main__":
    main()