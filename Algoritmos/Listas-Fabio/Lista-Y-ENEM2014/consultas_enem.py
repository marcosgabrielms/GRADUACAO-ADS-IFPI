from functools import reduce

CAMPOS = [
    'nome', 'municipio', 'uf', 'rede', 'permanencia', 
    'nivel_socio_economico', 'media_objetivas', 'linguagens', 
    'matematica', 'ciencias_natureza', 'humanas', 'redacao'
]

AREAS_NOTAS = ['media_objetivas', 'linguagens', 'matematica', 'ciencias_natureza', 'humanas', 'redacao']

def carregar_e_normalizar_dados(caminho_arquivo):
    dados_escolas = []
    try:
        with open(caminho_arquivo, 'r', encoding='latin-1') as f:
            next(f)
            for linha in f:
                if not linha.strip():
                    continue
                
                valores = linha.strip().split(';')
                dados_linha = valores[1:]

                if len(dados_linha) == len(CAMPOS):
                    escola = dict(zip(CAMPOS, dados_linha))
                    
                    for area in AREAS_NOTAS:
                        try:
                            escola[area] = float(escola[area].replace(',', '.'))
                        except (ValueError, TypeError):
                            escola[area] = 0.0
                    
                    dados_escolas.append(escola)
    except FileNotFoundError:
        print(f"ERRO: O arquivo de dados '{caminho_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return None
    
    if not dados_escolas:
        print("Atenção: Nenhum dado foi carregado.")
    else:
        print(f"Sucesso! {len(dados_escolas)} escolas foram carregadas.")

    return dados_escolas

def exibir_escolas(lista_escolas, limite=None):
    if not lista_escolas:
        print("\nNenhuma escola encontrada para os critérios informados.")
        return
    
    resultados = lista_escolas[:limite] if limite else lista_escolas

    print("\n--- Resultados da Consulta ---")
    for i, escola in enumerate(resultados):
        print(
            f"{i+1}. {escola['nome']} ({escola['municipio']}/{escola['uf']}) "
            f"- Rede: {escola['rede']} - Média Objetivas: {escola['media_objetivas']:.2f}"
        )
    print("----------------------------\n")

def consultar_top_n_por_uf(dados):
    try:
        n = int(input("Digite o número de escolas (N): "))
        uf = input("Digite a sigla do Estado (UF): ").upper()
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para N.")
        return

    escolas_filtradas = list(filter(lambda esc: esc['uf'] == uf, dados))
    escolas_ordenadas = sorted(escolas_filtradas, key=lambda esc: esc['media_objetivas'], reverse=True)
    
    exibir_escolas(escolas_ordenadas, limite=n)

def consultar_media_nacional_por_area(dados):
    print("\n--- Média Nacional por Área de Prova ---")
    for area in AREAS_NOTAS:
        notas = map(lambda esc: esc[area], dados)
        notas_validas = list(filter(lambda nota: nota > 0, notas))
        
        lista_de_notas = list(notas_validas)
        if not lista_de_notas:
            media = 0.0
        else:
            soma_total = reduce(lambda acumulador, valor: acumulador + valor, lista_de_notas)
            media = soma_total / len(lista_de_notas)
            
        print(f"- {area.replace('_', ' ').capitalize()}: {media:.2f}")
    print("--------------------------------------\n")

def buscar_escola_por_nome(dados):
    termo = input("Digite parte do nome da escola: ").lower()
    escolas_encontradas = list(filter(lambda esc: termo in esc['nome'].lower(), dados))
    
    exibir_escolas(escolas_encontradas)