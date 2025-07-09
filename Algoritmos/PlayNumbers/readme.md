# Play Numbers - Gerenciador de Vetores em Python

Este é um projeto acadêmico desenvolvido para a disciplina de Algoritmos e Programação. Trata-se de uma aplicação de console interativa, construída em Python, para realizar diversas operações em um vetor (lista) de números.

## 🚀 Funcionalidades

A aplicação oferece um menu completo com as seguintes operações:

* **1. Inicializar Vetor**: Permite criar um vetor de três formas:
    * Inserindo valores manualmente.
    * Gerando valores aleatórios dentro de uma faixa definida.
    * Carregando valores de um arquivo de texto.
* **2. Mostrar todos os valores**: Exibe o conteúdo atual do vetor.
* **3. Resetar Vetor**: Preenche o vetor com um valor padrão informado pelo usuário.
* **4. Ver quantidade de itens**: Mostra o número de elementos no vetor.
* **5. Ver Menor e Maior valores**: Encontra os valores mínimo e máximo e suas respectivas posições.
* **6. Somatório dos Valores**: Calcula a soma de todos os números no vetor.
* **7. Média dos Valores**: Calcula a média de todos os números no vetor.
* **8. Mostrar Valores Positivos**: Filtra e exibe apenas os números positivos e sua quantidade.
* **9. Mostrar Valores Negativos**: Filtra e exibe apenas os números negativos e sua quantidade.
* **10. Atualizar todos os valores**: Aplica transformações em massa no vetor, como multiplicar ou elevar a uma potência.
* **11. Adicionar Novo Valor**: Insere um novo número no final do vetor.
* **12. Remover Itens por Valor**: Remove todas as ocorrências de um valor específico.
* **13. Remover por Posição**: Remove um item de uma posição (índice) específica.
* **14. Editar valor por Posição**: Altera o valor em uma posição específica.
* **15. Salvar valores em arquivo**: Grava o estado atual do vetor em um arquivo `.txt`.
* **16. Ordenar Vetor**: Ordena o vetor em ordem crescente ou decrescente.
* **17. Embaralhar Vetor**: Reorganiza os itens do vetor de forma aleatória.
* **18. Sair**: Finaliza a aplicação, com a opção de salvar o trabalho atual.

## 📂 Estrutura do Projeto

O código é modularizado para facilitar a manutenção e a leitura:

* **`play_numbers_marcos.py`**: Arquivo principal da aplicação. Responsável por exibir o menu, gerenciar o loop de interação com o usuário e chamar as funcionalidades.
* **`operacoes_vetor.py`**: Módulo que contém o "coração" do projeto, com a implementação de todas as operações lógicas que podem ser realizadas no vetor.
* **`io_utils.py`**: Módulo de utilidades que centraliza as funções de entrada de dados, garantindo que as entradas do usuário sejam válidas e seguras.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* Módulos da biblioteca padrão: `random` e `functools`.

## ⚙️ Como Executar

Para rodar o projeto em sua máquina local, siga os passos abaixo:

1.  Certifique-se de ter o Python 3 instalado em seu sistema.
2.  Clone o repositório para a sua máquina.
3.  Pelo terminal, navegue até o diretório do projeto:
    ```bash
    cd Algoritmos/PlayNumbers
    ```
4.  Execute o script principal:
    ```bash
    python play_numbers_marcos.py
    ```
5.  O menu interativo será exibido. Siga as instruções e explore as funcionalidades!

## ✍️ Autor

* **Marcos Gabriel**
