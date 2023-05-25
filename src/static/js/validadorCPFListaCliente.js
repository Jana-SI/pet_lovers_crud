function validarCPF(cpf, cpfFormElement) {

    var strCPF = cpf.replace(/\D/g, ''), Soma = 0, Resto;

    if (strCPF == "00000000000" || strCPF == "11111111111" || strCPF == "22222222222" || strCPF == "33333333333" || strCPF == "44444444444" || strCPF == "55555555555" || strCPF == "66666666666" || strCPF == "77777777777" || strCPF == "88888888888" || strCPF == "99999999999") {
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
        cpfFormElement.setCustomValidity("CPF inválido!");
        cpfFormElement.reportValidity();
        return false;
    }

    else {
        cpfFormElement.setCustomValidity("");
        return true;
    }
}

const verificaCpf = async () => {

    const formAssociar = document.forms["formListaClientes"];
    const cpfFormElement = formAssociar['cliente'];
    const cpf = cpfFormElement.value;

    if (!cpf) {
        cpfFormElement.setCustomValidity("Campo CPF está vazio!")
        cpfFormElement.reportValidity()
    }

    else {
        resp = validarCPF(cpf, cpfFormElement);

        if (resp) {
            axios.post('/listar_cliente_verificando_cpf', {
                cpf: cpf
            }).then((response) => {
                if (response.data.cpfValido == "true") {
                    console.log(response.data);

                    cpfFormElement.setCustomValidity("")

                } else {
                    cpfFormElement.setCustomValidity("CPF não castrado!")
                    cpfFormElement.reportValidity()
                }
            }, (error) => {
                console.log(error)
            })
        }

    }

}