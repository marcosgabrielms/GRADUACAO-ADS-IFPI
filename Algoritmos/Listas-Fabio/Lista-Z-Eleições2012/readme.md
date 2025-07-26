# Análise de Eleições Proporcionais - Atividade PF-003

Esta atividade consiste na implementação de um script em Python para analisar os resultados da eleição para vereador, seguindo as regras do sistema eleitoral proporcional brasileiro. O estudo de caso utiliza dados hipotéticos baseados no pleito de 2012 em Teresina-PI.

O trabalho foi desenvolvido como parte da Atividade Individual "PF-003" para a disciplina de Algoritmos e Programação, do curso de Tecnologia em Análise e Desenvolvimento de Sistemas do Instituto Federal do Piauí (IFPI).

## Objetivo

> O objetivo, conforme definido no documento da atividade, é: "Verificar a capacidade interpretativa e de resolução, diante um problema/situação a ser automatizada por meio lógica de programação em software."

## Conceitos Abordados

O script simula o complexo sistema eleitoral proporcional, que determina os eleitos não apenas pela contagem individual de votos, mas pela força da votação total de seu partido ou coligação. Os cálculos centrais implementados são:

* **Quociente Eleitoral (QE):** Calculado pela soma de todos os votos válidos, dividida pelo número de cadeiras em disputa.
* **Quociente Partidário (QP):** Define o número de vagas iniciais para partidos ou coligações que atingiram o QE.
* **Distribuição das Sobras:** Regra de cálculo para as vagas restantes, dividindo os votos do partido pelo (número de vagas já obtidas + 1).

## Implementação

O script foi desenvolvido em **Python**, utilizando módulos padrão para manipulação de arquivos e interação com o sistema operacional.

1.  **Entrada de Dados:** O programa lê os dados de dois arquivos no formato `.csv`:
    * `partidos_coligacoes_the_2012.csv`: Contém a lista de todos os partidos e coligações.
    * `candidatos_e_votos_vereador_THE_2012.csv`: Contém os dados detalhados de cada candidato, incluindo nome, número, partido e total de votos.

2.  **Processamento:** Os dados são carregados em memória utilizando estruturas como listas e dicionários. Todos os cálculos (QE, QP, Sobras) são realizados de forma sequencial para determinar a distribuição final das vagas.

3.  **Interface de Usuário:** Para facilitar a visualização dos resultados, foi implementado um **menu interativo** no terminal. O programa primeiro processa todos os dados e, em seguida, permite que o usuário escolha qual consulta específica deseja visualizar.

## Funcionalidades do Script

O menu principal oferece as seguintes consultas, baseadas nas questões da atividade:

* **a) Total de Votos Válidos:** Exibe a soma de todos os votos válidos.
* **b) Quociente Eleitoral (QE):** Mostra o QE calculado para a eleição.
* **c) Total de Votos por Coligação:** Lista cada coligação e o total de votos recebidos.
* **d) Vagas Iniciais por Quociente Partidário (QP):** Apresenta a primeira distribuição de vagas.
* **e) Resultado Final da Distribuição de Vagas:** Mostra a quantidade final de vagas de cada coligação após a distribuição das sobras.
* **f) Vereadores Eleitos (Sistema Proporcional):** Imprime a lista final dos candidatos eleitos segundo todas as regras.
* **g) Vereadores que seriam Eleitos (Sistema Majoritário):** Apresenta uma simulação de como seria o resultado caso apenas os mais votados fossem eleitos.
* **T) Ver Todos os resultados:** Exibe todos os relatórios acima de uma só vez.
* **S) Sair:** Encerra o programa.

## Tecnologias Utilizadas

* **Python 3**
* Módulo `csv` (para leitura de dados)
* Módulo `os` (para limpeza do terminal na interface do menu)
