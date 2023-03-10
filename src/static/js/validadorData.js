function calcularIdade(nascimento){

    const dataAtual = new Date();

    var anoAtual = dataAtual.getFullYear();
    var anoNascimentoParts = nascimento.split('-');

    var diaNascimento = anoNascimentoParts[2];
    var mesNascimento = anoNascimentoParts[1];
    var anoNascimento = anoNascimentoParts[0];

    var idade = anoAtual - anoNascimento;

    var mesAtual = dataAtual.getMonth() + 1;
    var diaAtual = dataAtual.getDate();

    if(mesAtual < mesNascimento){
        idade--;
    }

    else{
        if(mesAtual == mesNascimento){
            if(diaAtual < diaNascimento){
                idade--;
            }
            else{
                return idade;
            }
        }
    }

    return idade;
}

const verificarData = async () => {
    
    const nascimento = document.getElementById('nascimento').value;

    idade = calcularIdade(nascimento);
    
    if(idade > 100){
        console.log("data invalida - ",idade)
    }

    if(idade < 0 ){
        console.log("data invalida - ",idade)
    }

    else{
        console.log(idade)
    }
}