function tipoFormatado(tipo){
    return tipo.replace(/_/g, ' ');
}

const tipo = document.querySelectorAll('.tipo');

for (let i = 0; i < tipo.length; i++) {

    tipo[i].textContent = tipoFormatado(tipo[i].innerText);
    
}