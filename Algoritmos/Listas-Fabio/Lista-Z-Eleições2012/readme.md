# Análise de Eleições Proporcionais - Atividade PF-003

Este projeto consiste na implementação de um script em Python para analisar os resultados da eleição para vereador, seguindo as regras do sistema eleitoral proporcional brasileiro. O estudo de caso utiliza dados hipotéticos baseados no pleito de 2012 em Teresina-PI.

[cite_start]O trabalho foi desenvolvido como parte da Atividade Individual "PF-003" para a disciplina de Algoritmos e Programação [cite: 2, 3][cite_start], do curso de Tecnologia em Análise e Desenvolvimento de Sistemas do Instituto Federal do Piauí (IFPI)[cite: 1, 2].

## Objetivo

> [cite_start]O objetivo, conforme definido no documento da atividade, é: "Verificar a capacidade interpretativa e de resolução, diante um problema/situação a ser automatizada por meio lógica de programação em software." [cite: 5, 6]

## Conceitos Abordados

[cite_start]O script simula o complexo sistema eleitoral proporcional, que determina os eleitos não apenas pela contagem individual de votos, mas pela força da votação total de seu partido ou coligação. [cite: 7, 8] Os cálculos centrais implementados são:

* [cite_start]**Quociente Eleitoral (QE):** Calculado pela soma de todos os votos válidos, dividida pelo número de cadeiras em disputa. [cite: 11]
* [cite_start]**Quociente Partidário (QP):** Define o número de vagas iniciais para partidos ou coligações que atingiram o QE. [cite: 11]
* [cite_start]**Distribuição das Sobras:** Regra de cálculo para as vagas restantes, dividindo os votos do partido pelo (número de vagas já obtidas + 1). [cite: 11]

## Implementação

O script foi desenvolvido em **Python**, utilizando módulos padrão para manipulação de arquivos e interação com o sistema operacional.

1.  **Entrada de Dados:** O programa lê os dados de dois arquivos no formato `.csv`:
    * [cite_start]`partidos_coligacoes_the_2012.csv`: Contém a lista de todos os partidos e coligações. [cite: 19, 20]
    * [cite_start]`candidatos_e_votos_vereador_THE_2012.csv`: Contém os dados detalhados de cada candidato, incluindo nome, número, partido e total de votos. [cite: 21, 22]

2.  [cite_start]**Processamento:** Os dados são carregados em memória utilizando estruturas como listas e dicionários. [cite: 28, 39] [cite_start]Todos os cálculos (QE, QP, Sobras) são realizados de forma sequencial para determinar a distribuição final das vagas. [cite: 45, 53, 56]

3.  **Interface de Usuário:** Para facilitar a visualização dos resultados, foi implementado um **menu interativo** no terminal. O programa primeiro processa todos os dados e, em seguida, permite que o usuário escolha qual consulta específica deseja visualizar.

## Funcionalidades do Script

O menu principal oferece as seguintes consultas, baseadas nas questões da atividade:

* [cite_start]**a) Total de Votos Válidos:** Exibe a soma de todos os votos válidos. [cite: 43]
* [cite_start]**b) Quociente Eleitoral (QE):** Mostra o QE calculado para a eleição. [cite: 45]
* [cite_start]**c) Total de Votos por Coligação:** Lista cada coligação e o total de votos recebidos. [cite: 46]
* [cite_start]**d) Vagas Iniciais por Quociente Partidário (QP):** Apresenta a primeira distribuição de vagas. [cite: 53]
* [cite_start]**e) Resultado Final da Distribuição de Vagas:** Mostra a quantidade final de vagas de cada coligação após a distribuição das sobras. [cite: 56]
* [cite_start]**f) Vereadores Eleitos (Sistema Proporcional):** Imprime a lista final dos candidatos eleitos segundo todas as regras. [cite: 61]
* [cite_start]**g) Vereadores que seriam Eleitos (Sistema Majoritário):** Apresenta uma simulação de como seria o resultado caso apenas os mais votados fossem eleitos. [cite: 62]
* **T) Ver Todos os resultados:** Exibe todos os relatórios acima de uma só vez.
* **S) Sair:** Encerra o programa.

## Tecnologias Utilizadas

* **Python 3**
* Módulo `csv` (para leitura de dados)
* Módulo `os` (para limpeza do terminal na interface do menu)