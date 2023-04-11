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

let verificarData = async () => {
    
    var nascimento = document.getElementById('nascimento').value;
    console.log(nascimento)
    const formAtualiza = document.forms["formAtualiza"];
    const nascFormElement = formAtualiza['nascimento'];
    var errorData;

    var idade = calcularIdade(nascimento);

    if((idade < 0) || (idade > 100)){
        errorData = "Data de nascimento inválida!";
        document.getElementById("errorData").innerHTML = errorData;
        nascFormElement.setCustomValidity("Data de nascimento inválida!");
        nascFormElement.reportValidity();
    }

    else{
        errorData = idade + ' anos';
        document.getElementById("errorData").innerHTML = errorData;
        nascFormElement.setCustomValidity("");
    }
}