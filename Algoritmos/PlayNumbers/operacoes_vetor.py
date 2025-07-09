import random
from functools import reduce
from io_utils import obter_numero, pressione_enter_para_continuar

def executar_inicializacao(vetor):
    print("\n--- Inicializar Vetor ---")
    print("1. Inserir valores manualmente")
    print("2. Gerar valores automáticos")
    print("3. Carregar de arquivo")
    sub_opcao = obter_numero("Sua escolha: ", int)

    if sub_opcao == 1:
        return _inicializar_manual()
    elif sub_opcao == 2:
        return _inicializar_automatico()
    elif sub_opcao == 3:
        return _carregar_de_arquivo()
    else:
        print("Opção de inicialização inválida.")
        return vetor

def executar_atualizacao(vetor):
    if not vetor:
        print("Vetor vazio. Inicialize o vetor primeiro.")
        return vetor

    print("\n--- Atualizar Valores ---")
    print("1. Multiplicar por um valor")
    print("2. Elevar a um valor")
    print("3. Substituir negativos por aleatórios")
    sub_opcao = obter_numero("Sua escolha: ", int)
    
    if sub_opcao == 1:
        fator = obter_numero("Digite o fator de multiplicação: ")
        return list(map(lambda n: n * fator, vetor))
    elif sub_opcao == 2:
        expoente = obter_numero("Digite o expoente: ")
        return list(map(lambda n: n ** expoente, vetor))
    elif sub_opcao == 3:
        min_val = obter_numero("Valor mínimo para aleatório: ")
        max_val = obter_numero("Valor máximo para aleatório: ")
        return list(map(lambda n: random.uniform(min_val, max_val) if n < 0 else n, vetor))
    else:
        print("Opção de atualização inválida.")
        return vetor

def mostrar_todos(vetor):
    print("\n>> Valores no vetor:")
    print(vetor)
    return vetor

def resetar_vetor(vetor):
    valor_padrao = obter_numero("Digite o valor padrão para resetar o vetor: ")
    return [valor_padrao] * len(vetor) if vetor else []

def ver_quantidade(vetor):
    print(f"\nO vetor possui {len(vetor)} itens.")
    return vetor

def ver_maior_menor(vetor):
    if not vetor:
        print("Vetor vazio.")
        return vetor
    
    maior = reduce(lambda a, b: a if a > b else b, vetor)
    menor = reduce(lambda a, b: a if a < b else b, vetor)
    
    print(f"\nMaior valor: {maior} (na posição {vetor.index(maior)})")
    print(f"Menor valor: {menor} (na posição {vetor.index(menor)})")
    return vetor

def ver_somatorio(vetor):
    if not vetor:
        print("Vetor vazio. Somatório é 0.")
        return vetor
    total = reduce(lambda acc, item: acc + item, vetor, 0)
    print(f"\nO somatório dos valores é: {total}")
    return vetor

def ver_media(vetor):
    if not vetor:
        print("Vetor vazio. Média é 0.")
        return vetor
    soma = reduce(lambda acc, item: acc + item, vetor, 0)
    media = soma / len(vetor)
    print(f"\nA média dos valores é: {media:.2f}")
    return vetor

def ver_positivos(vetor):
    positivos = list(filter(lambda n: n > 0, vetor))
    print(f"\nValores Positivos: {positivos}")
    print(f"Quantidade: {len(positivos)}")
    return vetor

def ver_negativos(vetor):
    negativos = list(filter(lambda n: n < 0, vetor))
    print(f"\nValores Negativos: {negativos}")
    print(f"Quantidade: {len(negativos)}")
    return vetor

def adicionar_novo_valor(vetor):
    novo_valor = obter_numero("Digite o novo valor a ser adicionado: ")
    vetor.append(novo_valor)
    print(f"Valor {novo_valor} adicionado.")
    return vetor

def remover_por_valor(vetor):
    if not vetor:
        print("Vetor vazio.")
        return vetor
    valor_a_remover = obter_numero("Digite o valor exato a ser removido: ")
    tamanho_antes = len(vetor)
    vetor_novo = list(filter(lambda v: v != valor_a_remover, vetor))
    if len(vetor_novo) < tamanho_antes:
        print(f"Todas as ocorrências de {valor_a_remover} foram removidas.")
    else:
        print(f"Valor {valor_a_remover} não encontrado.")
    return vetor_novo

def remover_por_posicao(vetor):
    if not vetor:
        print("Vetor vazio.")
        return vetor
    posicao = obter_numero("Digite a posição a ser removida: ", int)
    if 0 <= posicao < len(vetor):
        removido = vetor.pop(posicao)
        print(f"Valor {removido} da posição {posicao} foi removido.")
    else:
        print("Posição inválida.")
    return vetor

def editar_por_posicao(vetor):
    if not vetor:
        print("Vetor vazio.")
        return vetor
    posicao = obter_numero("Digite a posição a ser editada: ", int)
    if 0 <= posicao < len(vetor):
        novo_valor = obter_numero(f"Digite o novo valor para a posição {posicao}: ")
        vetor[posicao] = novo_valor
        print("Valor atualizado.")
    else:
        print("Posição inválida.")
    return vetor
    
def ordenar_vetor(vetor):
    if not vetor:
        print("Vetor vazio.")
        return vetor
    
    ordem = input("Ordenar em ordem crescente (c) ou decrescente (d)? ").lower()
    if ordem == 'd':
        return sorted(vetor, reverse=True)
    return sorted(vetor)

def embaralhar_vetor(vetor):
    if not vetor:
        print("Vetor vazio.")
        return vetor
        
    vetor_copia = vetor[:]
    random.shuffle(vetor_copia)
    return vetor_copia

def salvar_em_arquivo(vetor):
    if not vetor:
        print("Vetor vazio. Nada para salvar.")
        return vetor
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: dados.txt): ")
    try:
        with open(nome_arquivo, 'w') as f:
            for item in vetor:
                f.write(f"{item}\n")
        print(f"Vetor salvo com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")
    return vetor

def _inicializar_manual():
    tamanho = obter_numero("Quantos valores deseja inserir? ", int)
    vetor = []
    for i in range(tamanho):
        valor = obter_numero(f"Digite o valor #{i+1}: ")
        vetor.append(valor)
    return vetor

def _inicializar_automatico():
    tamanho = obter_numero("Tamanho do vetor: ", int)
    min_val = obter_numero("Valor mínimo: ")
    max_val = obter_numero("Valor máximo: ")
    return [random.uniform(min_val, max_val) for _ in range(tamanho)]

def _carregar_de_arquivo():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(nome_arquivo, 'r') as f:
            return [float(linha.strip()) for linha in f]
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return []