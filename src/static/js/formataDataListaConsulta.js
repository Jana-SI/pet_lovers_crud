function dataAtualFormatada(data){

    data = data.split('-');

    var dia = data[2],
    mes = data[1],
    ano = data[0];
    
    var diaF = (dia.length == 1) ? '0'+dia : dia,
    mesF = (mes.length == 1) ? '0'+mes : mes,
    anoF = ano;

    return diaF+"/"+mesF+"/"+anoF;
}

function calcularIdade(nascimento){

    const dataAtual = new Date();

    var anoAtual = dataAtual.getFullYear();
    var anoNascimentoParts = nascimento.split('/');

    var diaNascimento = anoNascimentoParts[0];
    var mesNascimento = anoNascimentoParts[1];
    var anoNascimento = anoNascimentoParts[2];

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


const data = document.querySelectorAll('.data');
const nascimento = document.querySelectorAll('.nascimento');
const idade = document.querySelectorAll('.idade');

for (let i = 0; i < data.length; i++) {

    data[i].textContent = dataAtualFormatada(data[i].innerText);
    
}

for (let i = 0; i < nascimento.length; i++) {

    nascimento[i].textContent = dataAtualFormatada(nascimento[i].innerText);
    idade[i].textContent = calcularIdade(nascimento[i].textContent);
    
}