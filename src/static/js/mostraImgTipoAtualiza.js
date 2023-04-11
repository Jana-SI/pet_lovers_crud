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
        document.getElementById('imgTipo').src = ave;
    } 

    if (tipo == "cachorro") {
        document.getElementById('imgTipo').src = cachorro;
    }

    if (tipo == "chinchila") {
        document.getElementById('imgTipo').src = chinchila;
    }

    if (tipo == "coelho") {
        document.getElementById('imgTipo').src = coelho; 
    }

    if (tipo == "gato") {
        document.getElementById('imgTipo').src = gato;
    }

    if (tipo == "exotico") {
        document.getElementById('imgTipo').src = exotico;
    }

    if (tipo == "hamster") {
        document.getElementById('imgTipo').src = hamster;
    }

    if (tipo == "peixe") {
        document.getElementById('imgTipo').src = peixe;
    }

    if (tipo == "porquinho_da_india") {
        document.getElementById('imgTipo').src = porquinho_da_india;
    }

    if(tipo == "" || tipo == "nao-declarado"){
        document.getElementById('imgTipo').src = "";
    }
}