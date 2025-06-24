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