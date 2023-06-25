function mostraImgTipo(tipo) {

    var ave = "/static//img/ave.png",
        canino = "/static//img/canino.png",
        exotico = "/static//img/exotico.png",
        felino = "/static//img/felino.png",
        lagomorfo = "/static//img/lagomorfo.png",
        peixe = "/static//img/peixe.png",
        roedor = "/static//img/roedor.png",
        naoDeclarado = "/static//img/nao_informado.png";

    if (tipo == "ave") {
        document.getElementById('imgTipo').src = ave;
    } 

    if (tipo == "canino") {
        document.getElementById('imgTipo').src = canino;
    }

    if (tipo == "exotico") {
        document.getElementById('imgTipo').src = exotico;
    }

    if (tipo == "felino") {
        document.getElementById('imgTipo').src = felino;
    }

    if (tipo == "lagomorfo") {
        document.getElementById('imgTipo').src = lagomorfo; 
    }

    if (tipo == "peixe") {
        document.getElementById('imgTipo').src = peixe;
    }  

    if (tipo == "roedor") {
        document.getElementById('imgTipo').src = roedor;
    }

    if(tipo == "nao-declarado"){
        document.getElementById('imgTipo').src = naoDeclarado;
    }

    if(tipo == ""){
        document.getElementById('imgTipo').src = "";
    }
}