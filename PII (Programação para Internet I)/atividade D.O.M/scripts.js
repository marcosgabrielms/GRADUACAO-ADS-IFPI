function getById(id) {
    return document.getElementById(id);
}

function getBotaoClicavel(id, funcao) {
    getById(id).addEventListener('click', funcao);
    return getById(id);
}

let botaoCriarParagrafo = 
    getBotaoClicavel('botaoCriarParagrafo', criarParagrafo);


function criarParagrafo() {

    let p1 = document.createElement('p');

    p1.innerHTML = 'Hello Wolrd 2';
    p1.id = 'p1'

    getById('resultado1').appendChild(p1);
}

let botaoCriarElemento = 
    getBotaoClicavel('botaoCriarElemento', criarElemento);

function criarElemento() {
    let elemento = getById('tagElemento').value;
    //crio o elemnto
    let elementoCriado = document.createElement(elemento);

    elementoCriado.id = getById('id').value;
    elementoCriado.innerText = getById('texto').value;

    elementoCriado.setAttribute(getById('atributo').value, getById('valor').value);

    let pai = getById('pai').value;

    getById('resultado2').appendChild(elementoCriado);
}

let botaoAdicionarTarefa = 
    getBotaoClicavel('botaoAdicionarTarefa', adicionarTarefa);

let contador = 1;

function adicionarTarefa() {
    let descricao = getById('descricao').value;
    let percentual = getById('percentual').value;

    //crio a linha da tabela
    let tr = document.createElement('tr')
    tr.id = contador;

    // Crio as colunas
    let tdContador = document.createElement('td');
    tdContador.inneText = contador;

    // Descrição
    let tdDescricao = document.createElement('td');
    tdDescricao.innerText = descricao;

    //Percetual
    let tdPercentual = document.createElement('td');
    tdPercentual.innerText = percentual + '%';

    // Ação
    let tdAcao = document.createElement('td');
    let botaoExcluir = document.createElement('button');
    botaoExcluir.innerText = 'Excluir';
    //botaoExcluir.onclick = excluirTarefa();

    tdAcao.appendChild(botaoExcluir);

    tr.appendChild(tdContador);
    tr.appendChild(tdDescricao);
    tr.appendChild(tdPercentual);
    tr.appendChild(tdAcao);
    
    contador++;

    getById('tarefas').appendChild(tr);

}

