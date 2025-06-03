from io_utils import *

def mostrar_menu():
    print("\n===Menu de Opções ===")
    print("1. Calcular perda de peso")
    print("2.Sair")

def executar_calculo():
    print("\n=== Cálculo de perda de Peso ===")

    sexo = ler_sexo()
    dias_semana = ler_inteiro_positivo("Quantos dias por semana irá treinar?: ")
    minutos_dias = ler_inteiro_positivo("Quantos minutos por dia irá treinar?: ")
    quilos_perder = ler_inteiro_positivo("Quantos quilos deseja perder?: ")
    percentual_transport = ler_percentual_transport()

    minutos_transport = (minutos_dias * percentual_transport) // 100
    minutos_escada = minutos_dias - minutos_transport

    cal_transport = calorias_por_minutos(sexo, "transport")
    cal_escada = calorias_por_minutos(sexo, "escada")

    calorias_por_semana = gasto_semanal(
        minutos_escada, minutos_transport,
        cal_escada, cal_transport,
        dias_semana
    )

    semanas =  semanas_necessarias(quilos_perder, calorias_por_semana)

    print(f"\nResultado: ")
    print(f"Para perder {quilos_perder} kg, treine por aproximadamente {semanas} semanas.")
    print(f"Treino diário: {minutos_transport} mins de Transport e {minutos_escada} mins de Escada.")
    print(f"Frequência semanal: {dias_semana} dias/semana, {minutos_dias} min/dia")

def main ():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção:").strip()

        if opcao == "1":
            executar_calculo()
        elif opcao == "2":
            print("Encerrando o programa")
            break    
        else: 
            print("Opção inválida. Escolha 1 ou 2")

if __name__ == "__main__":
    main()