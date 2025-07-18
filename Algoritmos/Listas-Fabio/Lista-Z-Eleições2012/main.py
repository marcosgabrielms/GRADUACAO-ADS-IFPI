import csv
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados_e_calcular_tudo():
    script_dir = os.path.dirname(__file__)
    caminho_partidos = os.path.join(script_dir, 'partidos_coligacoes_the_2012.csv')
    caminho_candidatos = os.path.join(script_dir, 'candidatos_e_votos_vereador_THE_2012.csv')
    
    VAGAS_TOTAIS = 29

    coligacoes = []
    with open(caminho_partidos, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if nome_coligacao := row[0].strip():
                coligacoes.append({
                    'coligacao': nome_coligacao, 'total_votos': 0, 
                    'qtd_vagas': 0, 'votos_sobra_total': 0
                })

    candidatos = []
    with open(caminho_candidatos, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            candidatos.append({
                'nome': row[0].strip(), 'numero': int(row[1]),
                'partido': row[2].strip(), 'coligacao': row[3].strip(),
                'total_votos': int(row[4])
            })
    
    candidatos.sort(key=lambda c: c['total_votos'], reverse=True)

    total_votos_validos = sum(c['total_votos'] for c in candidatos)
    quociente_eleitoral = total_votos_validos // VAGAS_TOTAIS

    for coligacao in coligacoes:
        coligacao['total_votos'] = sum(c['total_votos'] for c in candidatos if c['coligacao'] == coligacao['coligacao'])

    vagas_distribuidas_qp = 0
    for coligacao in coligacoes:
        if coligacao['total_votos'] >= quociente_eleitoral:
            vagas_qp = coligacao['total_votos'] // quociente_eleitoral
            coligacao['qtd_vagas'] = vagas_qp
            vagas_distribuidas_qp += vagas_qp
    
    vagas_restantes = VAGAS_TOTAIS - vagas_distribuidas_qp

    for _ in range(vagas_restantes):
        maior_media = -1
        coligacao_vencedora = None
        for c in coligacoes:
            if c['total_votos'] >= quociente_eleitoral:
                media_atual = c['total_votos'] / (c['qtd_vagas'] + 1)
                if media_atual > maior_media:
                    maior_media = media_atual
                    coligacao_vencedora = c
        if coligacao_vencedora:
            coligacao_vencedora['qtd_vagas'] += 1

    eleitos_proporcional = []
    for coligacao in coligacoes:
        if vagas := coligacao['qtd_vagas']:
            cands_coligacao = [c for c in candidatos if c['coligacao'] == coligacao['coligacao']]
            eleitos_proporcional.extend(cands_coligacao[:vagas])
    
    eleitos_proporcional.sort(key=lambda c: c['total_votos'], reverse=True)
    eleitos_majoritario = candidatos[:VAGAS_TOTAIS]

    resultados = {
        "candidatos": candidatos,
        "coligacoes": coligacoes,
        "total_votos_validos": total_votos_validos,
        "quociente_eleitoral": quociente_eleitoral,
        "vagas_totais": VAGAS_TOTAIS,
        "eleitos_proporcional": eleitos_proporcional,
        "eleitos_majoritario": eleitos_majoritario,
    }
    return resultados

def exibir_todos_os_resultados(dados):
    print("--- a) Total de Votos Válidos ---")
    print(f"Total de votos válidos apurados: {dados['total_votos_validos']:,}".replace(",", "."))
    print("\n" + "="*50 + "\n")

    print("--- b) Quociente Eleitoral (QE) ---")
    print(f"Para {dados['vagas_totais']} vagas, o Quociente Eleitoral foi de: {dados['quociente_eleitoral']:,}".replace(",", "."))
    print("\n" + "="*50 + "\n")

    print("--- c) Total de Votos por Coligação ---")
    for c in sorted(dados['coligacoes'], key=lambda x: x['total_votos'], reverse=True):
        print(f"{c['coligacao']:<25} | {c['total_votos']:,} votos".replace(",", "."))
    print("\n" + "="*50 + "\n")

    print("--- d) Vagas Iniciais por Quociente Partidário (QP) ---")
    vagas_qp_totais = 0
    for c in dados['coligacoes']:
        if c['total_votos'] >= dados['quociente_eleitoral']:
            vagas_qp = c['total_votos'] // dados['quociente_eleitoral']
            vagas_qp_totais += vagas_qp
            print(f"{c['coligacao']:<25} | {vagas_qp} vaga(s) por QP")
    print("-" * 40)
    print(f"Total de vagas por QP: {vagas_qp_totais}")
    print(f"Vagas de sobra (distribuídas por média): {dados['vagas_totais'] - vagas_qp_totais}")
    print("\n" + "="*50 + "\n")

    print("--- e) Resultado Final da Distribuição de Vagas ---")
    for c in sorted(dados['coligacoes'], key=lambda x: x['total_votos'], reverse=True):
         print(f"{c['coligacao']:<25} | {c['qtd_vagas']} vaga(s) no total")
    print("-" * 40)
    print(f"Total de vagas distribuídas: {sum(c['qtd_vagas'] for c in dados['coligacoes'])}")
    print("\n" + "="*50 + "\n")

    print("--- f) Vereadores Eleitos (Sistema Proporcional) ---")
    for i, eleito in enumerate(dados['eleitos_proporcional']):
        print(f"{i+1: >2}º - {eleito['nome']:<30} | {eleito['coligacao']:<25} | {eleito['total_votos']:,} votos".replace(",", "."))
    print("\n" + "="*50 + "\n")

    print("--- g) Vereadores que seriam Eleitos (Sistema Majoritário) ---")
    for i, eleito in enumerate(dados['eleitos_majoritario']):
        print(f"{i+1: >2}º - {eleito['nome']:<30} | {eleito['partido']:<40} | {eleito['total_votos']:,} votos".replace(",", "."))


def mostrar_menu():
    print("\n--- Análise Eleições 2012 - Menu ---")
    print("Escolha uma consulta para exibir:")
    print("a) Total de Votos Válidos")
    print("b) Quociente Eleitoral (QE)")
    print("c) Total de Votos por Coligação")
    print("d) Vagas Iniciais por Quociente Partidário (QP)")
    print("e) Resultado Final da Distribuição de Vagas")
    print("f) Vereadores Eleitos (Sistema Proporcional)")
    print("g) Vereadores que seriam Eleitos (Sistema Majoritário)")
    print("-" * 30)
    print("T) Ver Todos os resultados de uma vez")
    print("S) Sair do programa")

def main():
    print("Carregando e processando dados eleitorais... Aguarde.")
    dados = carregar_dados_e_calcular_tudo()
    limpar_tela()

    while True:
        mostrar_menu()
        opcao = input("Digite a letra da opção desejada: ").upper()
        limpar_tela()

        if opcao == 'A':
            print("--- a) Total de Votos Válidos ---")
            print(f"Total de votos válidos apurados: {dados['total_votos_validos']:,}".replace(",", "."))
        
        elif opcao == 'B':
            print("--- b) Quociente Eleitoral (QE) ---")
            print(f"Para {dados['vagas_totais']} vagas, o Quociente Eleitoral foi de: {dados['quociente_eleitoral']:,}".replace(",", "."))

        elif opcao == 'C':
            print("--- c) Total de Votos por Coligação ---")
            for c in sorted(dados['coligacoes'], key=lambda x: x['total_votos'], reverse=True):
                print(f"{c['coligacao']:<25} | {c['total_votos']:,} votos".replace(",", "."))

        elif opcao == 'D':
            print("--- d) Vagas Iniciais por Quociente Partidário (QP) ---")
            vagas_qp_totais = 0
            for c in dados['coligacoes']:
                if c['total_votos'] >= dados['quociente_eleitoral']:
                    vagas_qp = c['total_votos'] // dados['quociente_eleitoral']
                    vagas_qp_totais += vagas_qp
                    print(f"{c['coligacao']:<25} | {vagas_qp} vaga(s) por QP")
            print("-" * 40)
            print(f"Total de vagas por QP: {vagas_qp_totais}")
            print(f"Vagas de sobra (distribuídas por média): {dados['vagas_totais'] - vagas_qp_totais}")
            
        elif opcao == 'E':
            print("--- e) Resultado Final da Distribuição de Vagas ---")
            for c in sorted(dados['coligacoes'], key=lambda x: x['total_votos'], reverse=True):
                 print(f"{c['coligacao']:<25} | {c['qtd_vagas']} vaga(s) no total")
            print("-" * 40)
            print(f"Total de vagas distribuídas: {sum(c['qtd_vagas'] for c in dados['coligacoes'])}")

        elif opcao == 'F':
            print("--- f) Vereadores Eleitos (Sistema Proporcional) ---")
            for i, eleito in enumerate(dados['eleitos_proporcional']):
                print(f"{i+1: >2}º - {eleito['nome']:<30} | {eleito['coligacao']:<25} | {eleito['total_votos']:,} votos".replace(",", "."))

        elif opcao == 'G':
            print("--- g) Vereadores que seriam Eleitos (Sistema Majoritário) ---")
            for i, eleito in enumerate(dados['eleitos_majoritario']):
                print(f"{i+1: >2}º - {eleito['nome']:<30} | {eleito['partido']:<40} | {eleito['total_votos']:,} votos".replace(",", "."))

        elif opcao == 'T':
            exibir_todos_os_resultados(dados)

        elif opcao == 'S':
            print("Programa finalizado. Até logo!")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma das letras do menu.")
        
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

if __name__ == "__main__":
    main()