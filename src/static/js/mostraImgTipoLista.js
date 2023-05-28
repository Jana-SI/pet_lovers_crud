function mostraImgTipo(tipo) {

    var ave = {
        src: "/static//img/ave.png",
        title: "Ave"
    };
    var cachorro = {
        src: "/static//img/cachorro.png",
        title: "Cachorro"
    };
    var chinchila = {
        src: "/static//img/chinchila.png",
        title: "Chinchila"
    };
    var coelho = {
        src: "/static//img/coelho.png",
        title: "Coelho"
    };
    var gato = {
        src: "/static//img/gato.png",
        title: "Gato"
    };
    var exotico = {
        src: "/static//img/exotico.png",
        title: "Exótico"
    };
    var hamster = {
        src: "/static//img/hamster.png",
        title: "Hamster"
    };
    var peixe = {
        src: "/static//img/peixe.png",
        title: "Peixe"
    };
    var porquinho_da_india = {
        src: "/static//img/porquinho_da_india.png",
        title: "Porquinho da Índia"
    };

    var naoDeclarado = {
        src: "/static//img/nao_informado.png",
        title: "Não declarado"
    };

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