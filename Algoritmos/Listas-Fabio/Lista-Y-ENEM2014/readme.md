# Análise de Dados do ENEM

Este projeto foi desenvolvido para realizar a leitura, processamento e consulta de dados do Exame Nacional do Ensino Médio (ENEM). O sistema é composto por um arquivo principal que orquestra as operações, utilizando módulos de utilidades para interagir com os arquivos de dados.

## 🎯 Objetivo

O objetivo principal é fornecer uma interface de consulta para extrair informações específicas das notas do ENEM, utilizando uma base de dados distribuída em arquivos de texto.

## ⚙️ Funcionamento

O projeto opera com base em uma arquitetura modular, dividida em três componentes principais:

1.  **Arquivo Principal (`main.py`)**:
    * É o ponto de entrada do programa.
    * Responsável por apresentar o menu de opções ao usuário e gerenciar o fluxo de execução.
    * Invoca as funções dos módulos de utilidades (`io_utils`) para obter os dados necessários e exibir os resultados.

2.  **Módulo de Consultas (`consultas_enem.py`)**:
    * Funciona como uma biblioteca de utilidades (I/O).
    * Contém funções especializadas para realizar buscas, filtros e consultas sobre os dados das escolas e suas respectivas notas.
    * Lê os dados processados pelo módulo `notas_por_escola_enem.py` para realizar suas operações.

3.  **Módulo de Leitura de Dados (`notas_por_escola_enem.py`)**:
    * Também atua como uma biblioteca de utilidades (I/O).
    * Sua principal responsabilidade é ler os arquivos de texto (`.txt`) que contêm os dados brutos das escolas.
    * Realiza o parsing (análise) e a organização desses dados em uma estrutura que possa ser facilmente manipulada pelos outros módulos do sistema.

### Fluxo de Execução

1.  O usuário executa o **arquivo principal**.
2.  O **arquivo principal** chama as funções em `notas_por_escola_enem.py` para carregar e preparar os dados dos arquivos de texto.
3.  Com os dados carregados, o **arquivo principal** utiliza as funções de `consultas_enem.py` para realizar as operações solicitadas pelo usuário (como buscar a nota de uma escola específica, listar as melhores escolas, etc.).
4.  Os resultados são retornados ao **arquivo principal** e exibidos ao usuário.

## 📁 Estrutura do Repositório
```
/
│
├── main.py                   # Arquivo principal que executa o programa
├── consultas_enem.py         # Módulo com funções de consulta
├── notas_por_escola_enem.py  # Módulo para leitura e processamento dos dados
├── dados/                      # Pasta contendo os arquivos de dados
│   └── notas_escolas.txt     # Arquivo de texto com os dados das escolas
│
└── README.md                 # Este arquivo
```
