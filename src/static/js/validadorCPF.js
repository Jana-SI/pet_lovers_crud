function validarCPF(cpf, cpfFormElement) {

    var strCPF = cpf.replace(/\D/g, ''), Soma = 0, Resto, errorCPF;

    if (strCPF == "00000000000" || strCPF == "11111111111" || strCPF == "22222222222" || strCPF == "33333333333" || strCPF == "44444444444" || strCPF == "55555555555" || strCPF == "66666666666" || strCPF == "77777777777" || strCPF == "88888888888" || strCPF == "99999999999") {
        errorCPF = 'CPF inválido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        cpfFormElement.setCustomValidity("CPF inválido!");
        cpfFormElement.reportValidity();
        return false;
    }

    for (i = 1; i <= 9; i++) {
        Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);
    }

    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) {
        Resto = 0;
    }

    if (Resto != parseInt(strCPF.substring(9, 10))) {
        errorCPF = 'CPF inválido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        cpfFormElement.setCustomValidity("CPF inválido!");
        cpfFormElement.reportValidity();
        return false;
    }

    Soma = 0;

    for (i = 1; i <= 10; i++) {
        Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (12 - i);
    }

    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) {
        Resto = 0;
    }

    if (Resto != parseInt(strCPF.substring(10, 11))) {
        errorCPF = 'CPF inválido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        cpfFormElement.setCustomValidity("CPF inválido!");
        cpfFormElement.reportValidity();
        return false;
    }

    else {
        errorCPF = 'CPF valido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        cpfFormElement.setCustomValidity("");
        return true;
    }
}

const verificaCpf = async () => {

    const formCadastro = document.forms["formCadastro"];
    const cpfFormElement = formCadastro['cpf'];
    const cpf = cpfFormElement.value;

    if (!cpf) {
        cpfFormElement.setCustomValidity("Campo CPF está vazio!")
        cpfFormElement.reportValidity()
    }

    else {
        resp = validarCPF(cpf, cpfFormElement);

        if (resp) {
            axios.post('/cadastro_cliente_verificando_cpf', {
                cpf: cpf
            }).then((response) => {
                if (response.data.cpfValido == "true") {

                    cpfFormElement.setCustomValidity("CPF já castrado!")
                    cpfFormElement.reportValidity()
                    document.getElementById("btnCadCadastrar").disabled = true;

                } else {
                    cpfFormElement.setCustomValidity("")
                    document.getElementById("btnCadCadastrar").disabled = false;
                }
            }, (error) => {
                console.log(error)
            })
        }
    }

}