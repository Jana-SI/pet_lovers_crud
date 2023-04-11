function mostraImgTipo(tipo) {

    var ave = "/static//img/ave.png",
        cachorro = "/static//img/cachorro.png",
        chinchila = "/static//img/chinchila.png",
        coelho = "/static//img/coelho.png",
        gato = "/static//img/gato.png",
        exotico = "/static//img/exotico.png",
        hamster = "/static//img/hamster.png",
        peixe = "/static//img/peixe.png",
        porquinho_da_india = "/static//img/porquinho_da_india.png";

    if (tipo == "ave") {
        return ave;
    } 

    if (tipo == "cachorro") {
        return cachorro;
    }

    if (tipo == "chinchila") {
        return chinchila;
    }

    if (tipo == "coelho") {
        return coelho; 
    }

    if (tipo == "gato") {
        return gato;
    }

    if (tipo == "exotico") {
        return exotico;
    }

    if (tipo == "hamster") {
        return hamster;
    }

    if (tipo == "peixe") {
        return peixe;
    }

    if (tipo == "porquinho_da_india") {
        return porquinho_da_india;
    }

    if(tipo == "" || tipo == "nao-declarado"){
        return "";
    }
}

const tipo = document.querySelectorAll('.tipo');
const imgTipo = document.querySelectorAll('.imgTipo');

for (let i = 0; i < tipo.length; i++) {

    imgTipo[i].src = mostraImgTipo(tipo[i].innerText);
    
}