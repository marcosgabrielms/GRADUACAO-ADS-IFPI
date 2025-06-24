function getById(id) {
    return document.getElementById(id);
}

let botaoSolicitar = getById("botaoSolicitar");

botaoSolicitar.addEventListener("click", solicitiarConselho);


async function solicitiarConselho() {
    let url = "https://api.adviceslip.com/advice";

    try {
        let response = await fetch(url);
        
        if (!response.ok) {
            throw new Error('Response status: ${response.status}');
        }
        let json = await response.json();
        getById('conselho').innerText = json.slip.advice;
        //getById("conselho").innerText = json["slip"]["advice"];
    }catch (e){
        getById("erroConselho").innerTEXT = "Erro ao solicitar conselho";
        console.log(e.message)
    }
    
}

let botaoPesquisarPais = getById('botaoPesquisarPais');

botaoPesquisarPais.addEventListener("click", PesquisarPais);

async function PesquisarPais() {
    let url = "https://restcountries.com/v3.1/name/";

    try{
        let nomePais = getById("nomePais").value;
        url += nomePais;

        let response = await fetch(url);

        if (!response.ok) {
            throw new Error ('Response status: ${response.status}');
        }
        let json = await response.json();

        getById("bandeira").src = json[0].flags.png;
        getById("bandeira").alt = json[0].flags.alt;
        getById("nomeOficial").innerText = json[0].name.official;
       

    } catch(e) {
        getById("erroPais").innerText = "Erro ao pesquisar país";
        console.log(e.message);
    }
}