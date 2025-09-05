**a. Sim, seria mais do que interessante, é fundamental.** Em um sistema bancário, toda conta precisa estar associada a um titular (seja uma pessoa física ou jurídica). Fazer com que o objeto `Conta` tenha um atributo `titular` que é um objeto do tipo `Pessoa` é a maneira correta de modelar essa relação.
Isso garante a integridade dos dados e permite acessar facilmente as informações do titular a partir da conta (ex: `minhaConta.titular.nome`).

**b. Sim, também é muito interessante e comum.** Uma mesma pessoa pode ter várias contas em um banco (conta corrente, poupança, investimento, etc.). Por isso, faz todo o sentido que o objeto `Pessoa` possua um atributo para armazenar todas as suas contas.

O elemento da programação que melhor representaria esse conjunto de contas é um **array** (ou uma **lista**). Esse tipo de estrutura de dados permite que o atributo `contas` dentro do objeto `Pessoa` armazene uma coleção de objetos do tipo `Conta`. 
Ex: `clienteJoao.contas[0]` (primeira conta), `clienteJoao.contas[1]` (segunda conta), e assim por diante.