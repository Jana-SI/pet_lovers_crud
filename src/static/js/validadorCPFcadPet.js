function validarCPF(cpf, cpfFormElement) {

    var strCPF = cpf.replace(/\D/g, ''), Soma = 0, Resto;

    if (strCPF == "00000000000" || strCPF == "11111111111" || strCPF == "22222222222" || strCPF == "33333333333" || strCPF == "44444444444" || strCPF == "55555555555" || strCPF == "66666666666" || strCPF == "77777777777" || strCPF == "88888888888" || strCPF == "99999999999") {
        return false
    }

    for (i = 1; i <= 9; i++) {
        Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);
    }

    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) {
        Resto = 0;
    }

    if (Resto != parseInt(strCPF.substring(9, 10))) {
        return false
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
        return false
    }

    else {
        return true;
    }
}

const verificaCpf = async () => {

    const formCadastro = document.forms["formCadastro"];
    const cpfFormElement = formCadastro['donosPet'];
    const cpf = cpfFormElement.value;

    if (!cpf) {
        errorCPF = 'Campo CPF está vazio!!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        document.getElementById("btnCadCadastrar").disabled = true;
        document.getElementById("errorCPF").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px;padding: 10px;';
        cpfFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
    }

    else {
        resp = validarCPF(cpf, cpfFormElement);

        if (!resp) {
            cpfFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;';
            errorCPF = 'CPF inválido!';
            document.getElementById("errorCPF").innerHTML = errorCPF;
            document.getElementById("btnCadCadastrar").disabled = true;
            document.getElementById("errorCPF").style.cssText = 'color: red; border: 2px solid red; text-align: center; background: #fee; border-radius: 10px; padding: 10px;';
        } else {
            errorCPF = '';
            document.getElementById("errorCPF").innerHTML = errorCPF; document.getElementById("errorCPF").style.cssText = '';
            cpfFormElement.style.cssText = '';
        }

        if (resp) {
            axios.post('/cadastro_pet_verificando_cpf', {
                cpf: cpf
            }).then((response) => {
                if (response.data.cpfValido == "true") {

                    errorCPF = '';
                    document.getElementById("errorCPF").innerHTML = errorCPF; document.getElementById("errorCPF").style.cssText = '';
                    cpfFormElement.style.cssText = '';
                    document.getElementById("btnCadCadastrar").disabled = false;

                    const nascimento = document.getElementById('nascimento').value;
                    const idade = calcularIdade(nascimento);
                    const camposValidos = idade >= 0 && idade <= 100;

                    if (camposValidos) {
                        document.getElementById("btnCadCadastrar").disabled = false;
                    } else {
                        document.getElementById("btnCadCadastrar").disabled = true;
                    }

                } else {
                    errorCPF = 'CPF não castrado!';
                    document.getElementById("errorCPF").innerHTML = errorCPF;
                    document.getElementById("btnCadCadastrar").disabled = true;
                    document.getElementById("errorCPF").style.cssText = 'color: red; border: 2px solid red; text-align: center; background: #fee; border-radius: 10px; padding: 10px;';
                    cpfFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;';                    
                }
            }, (error) => {
                console.log(error)
            })
        }
    }

}