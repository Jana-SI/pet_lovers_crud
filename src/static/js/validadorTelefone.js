// validar input telefone da pagina cadastro de clientes
function validarTelefone(telefone, telefoneFormElement){

    var newTelefone = telefone.replace(/\D/g, ''), errorTelefone;

    if (!(newTelefone.length >= 10 && newTelefone.length <= 11)) {
		errorTelefone = 'Telefone inválido!';
        document.getElementById("errorTelefone").innerHTML = errorTelefone;
        telefoneFormElement.setCustomValidity("Telefone inválido!")
        return telefoneFormElement.reportValidity();
    }

    if (newTelefone.length == 11 && parseInt(newTelefone.substring(2, 3)) != 9) {
        errorTelefone = 'Telefone inválido!';
        document.getElementById("errorTelefone").innerHTML = errorTelefone;
        telefoneFormElement.setCustomValidity("Telefone inválido!")
        return telefoneFormElement.reportValidity();
    }

    for (var n = 0; n < 10; n++) {
        if (newTelefone == new Array(11).join(n) || newTelefone == new Array(12).join(n)) {
            errorTelefone = 'Telefone inválido!';
            document.getElementById("errorTelefone").innerHTML = errorTelefone;
            telefoneFormElement.setCustomValidity("Telefone inválido!")
            return telefoneFormElement.reportValidity();
        }
    }

    var codigosDDD = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 64, 63, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99];

    if (codigosDDD.indexOf(parseInt(newTelefone.substring(0, 2))) == -1) {
        errorTelefone = 'Telefone inválido!';
        document.getElementById("errorTelefone").innerHTML = errorTelefone;
        telefoneFormElement.setCustomValidity("Telefone inválido!")
        return telefoneFormElement.reportValidity();
    }

    if (newTelefone.length == 10 && [2, 3, 4, 5, 7].indexOf(parseInt(newTelefone.substring(2, 3))) == -1) {
        errorTelefone = 'Telefone inválido!';
        document.getElementById("errorTelefone").innerHTML = errorTelefone;
        telefoneFormElement.setCustomValidity("Telefone inválido!")
        return telefoneFormElement.reportValidity();
    }

    else{
        errorTelefone = 'Telefone valido!';
        document.getElementById("errorTelefone").innerHTML = errorTelefone;
        return telefoneFormElement.setCustomValidity("");
    }

}

const verificaTelefone = async () => {

    const formCadastro = document.forms["formCadastro"];
    const telefoneFormElement = formCadastro['telefone'];
    const telefone = telefoneFormElement.value;
    
    validarTelefone(telefone, telefoneFormElement);

    // codigo de comunicação js->flask pra fazer verificação se campo inserido ja tem no sistema

    // axios.post('/read/validarCpf', {
    //     cpf: cpf
    // })
    // .then((response) => {
    //     console.log("")
    //     console.log(response.data.cpfValido)
    //     if(response.data.cpfValido == "false"){
    //         cpfFormElement.setCustomValidity("cpf invalido")
    //         cpfFormElement.reportValidity()
    //     }else{
    //         cpfFormElement.setCustomValidity("")

    //     }
    // }, (error) => {
    //     console.log(error)
    // })


}