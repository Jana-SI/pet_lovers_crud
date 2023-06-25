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

    if (mesAtual < mesNascimento || (mesAtual === mesNascimento && diaAtual < diaNascimento)) {
        idade--; // Ajuste na idade se ainda não completou o ano atual
    }

    // Verifica se a idade é menor que 1 ano
    if (idade < 1) {
        return ''; // Retorna uma string vazia
    }

    return idade;
}

let verificarData = async () => {
    
    var nascimento = document.getElementById('nascimento').value;
    const formAtualiza = document.forms["formAtualiza"];
    const nascFormElement = formAtualiza['nascimento'];
    var errorData;

    var idade = calcularIdade(nascimento);

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

    else if(idade == ''){
        errorData = '';
        document.getElementById("errorData").innerHTML = errorData;
        nascFormElement.setCustomValidity("");
    }

    else{
        errorData = idade + ' anos';
        document.getElementById("errorData").innerHTML = errorData;
        nascFormElement.setCustomValidity("");
    }
}