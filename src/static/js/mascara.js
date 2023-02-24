// mascara cpf

function mascaraCPF(numCPF){
   
    var cpf = numCPF.value;
    
    if(isNaN(cpf[cpf.length-1])){ 
       numCPF.value = cpf.substring(0, cpf.length-1);
       return;
    }
    
    numCPF.setAttribute("maxlength", "14");
    if (cpf.length == 3 || cpf.length == 7) numCPF.value += ".";
    if (cpf.length == 11) numCPF.value += "-";
 
 }


// mascara de telefone

function mascaraTelefone(event) {
    let tecla = event.key;
    let telefone = event.target.value.replace(/\D+/g, "");

    if (/^[0-9]$/i.test(tecla)) {
        telefone = telefone + tecla;
        let tamanho = telefone.length;

        if (tamanho >= 12) {
            return false;
        }

        if (tamanho > 10) {
            telefone = telefone.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
        } else if (tamanho > 5) {
            telefone = telefone.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
        } else if (tamanho > 2) {
            telefone = telefone.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
        } else {
            telefone = telefone.replace(/^(\d*)/, "($1");
        }

        event.target.value = telefone;
    }

    if (!["Backspace", "Delete"].includes(tecla)) {
        return false;
    }
}