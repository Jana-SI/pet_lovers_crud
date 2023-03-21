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

const data = document.getElementById('data').innerText;

document.getElementById('data').innerText = dataAtualFormatada(data);