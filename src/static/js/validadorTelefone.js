function validarTelefone(telefone, telefoneFormElement) {

    var newTelefone = telefone.replace(/\D/g, ''), errorTelefone;

    if (!(newTelefone.length >= 10 && newTelefone.length <= 11)) {
        return false;
    }

    if (newTelefone.length == 11 && parseInt(newTelefone.substring(2, 3)) != 9) {
        return false;
    }

    for (var n = 0; n < 10; n++) {
        if (newTelefone == new Array(11).join(n) || newTelefone == new Array(12).join(n)) {
            return false;
        }
    }

    var codigosDDD = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 64, 63, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99];

    if (codigosDDD.indexOf(parseInt(newTelefone.substring(0, 2))) == -1) {
        return false;
    }

    if (newTelefone.length == 10 && [2, 3, 4, 5, 7].indexOf(parseInt(newTelefone.substring(2, 3))) == -1) {
        return false;
    }

    else {
        return true;
    }

}

const verificaTelefone = async () => {

    const formCadastro = document.forms["formCadastro"];
    const telefoneFormElement = formCadastro['telefone'];
    const telefone = telefoneFormElement.value;

    if (!telefone) {
        telefoneFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;';
        errorTelefone = 'Campo Telefone está vazio!!';
        document.getElementById("errorTelefone").innerHTML = errorTelefone;
        document.getElementById("btnCadCadastrar").disabled = true;
        document.getElementById("errorTelefone").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
    }

    else {

        resp = validarTelefone(telefone, telefoneFormElement);

        if (!resp) {
            telefoneFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;';
            errorTelefone = 'Telefone inválido!';
            document.getElementById("errorTelefone").innerHTML = errorTelefone;
            document.getElementById("btnCadCadastrar").disabled = true;
            document.getElementById("errorTelefone").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
        } else {
            telefoneFormElement.style.cssText = '';
            errorTelefone = '';
            document.getElementById("errorTelefone").innerHTML = errorTelefone;
            document.getElementById("errorTelefone").style.cssText = '';

            // Verifica se há erros no campo de CPF
            const cpfFormElement = formCadastro['cpf'];
            const cpf = cpfFormElement.value;
            const respCPF = validarCPF(cpf, cpfFormElement);

            if (respCPF) {
                if(verificaCpf()){
                    document.getElementById("btnCadCadastrar").disabled = false;
                }
            }
        }
    }
}