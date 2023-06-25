function mostraImgTipo(tipo) {

    var ave = {
        src: "/static//img/ave.png",
        title: "Ave"
    };
    var canino = {
        src: "/static//img/canino.png",
        title: "canino"
    };
    var exotico = {
        src: "/static//img/exotico.png",
        title: "Exótico"
    };
    var felino = {
        src: "/static//img/felino.png",
        title: "felino"
    };
    var lagomorfo = {
        src: "/static//img/lagomorfo.png",
        title: "lagomorfo"
    };
    var peixe = {
        src: "/static//img/peixe.png",
        title: "Peixe"
    };
    var roedor = {
        src: "/static//img/roedor.png",
        title: "roedor"
    };
    var naoDeclarado = {
        src: "/static//img/nao_informado.png",
        title: "Não declarado"
    };

    if (tipo == "ave") {
        return ave;
    } 

    if (tipo == "canino") {
        return canino;
    }

    if (tipo == "exotico") {
        return exotico;
    }

    if (tipo == "felino") {
        return felino;
    }

    if (tipo == "lagomorfo") {
        return lagomorfo; 
    }

    if (tipo == "peixe") {
        return peixe;
    }

    if (tipo == "roedor") {
        return roedor;
    }

    if (tipo == "nao-declarado"){
        return naoDeclarado;
    }

    if (tipo == ""){
        return "";
    }
}

const tipo = document.querySelectorAll('.tipo');
const imgTipo = document.querySelectorAll('.imgTipo');

for (let i = 0; i < tipo.length; i++) {
    const tipoAnimal = tipo[i].innerText;
    const imagem = mostraImgTipo(tipoAnimal);
    
    imgTipo[i].src = imagem.src;
    imgTipo[i].title = imagem.title;
}