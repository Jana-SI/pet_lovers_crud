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
    const formCadastro = document.forms["formCadastro"];
    const nascFormElement = formCadastro['nascimento'];
    var errorData;

    idade = calcularIdade(nascimento);

    if(idade < 0){
        errorData = "Data de nascimento inválida, idade negativa!";
        document.getElementById("errorData").innerHTML = errorData;
        nascFormElement.setCustomValidity("Data de nascimento inválida, idade negativa!");
        nascFormElement.reportValidity();
    }

    else if(idade > 100){
        errorData = "Data de nascimento inválida, idade passou dos 100 anos!";
        document.getElementById("errorData").innerHTML = errorData;
        nascFormElement.setCustomValidity("Data de nascimento inválida, idade passou dos 100 anos!");
        nascFormElement.reportValidity();
    }

    else{
        errorData = idade + ' anos';
        document.getElementById("errorData").innerHTML = errorData;
        nascFormElement.setCustomValidity("");
    }
}