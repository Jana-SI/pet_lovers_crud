// valida input cpf da pagina cadastro de clientes
function validarCPF(cpf, cpfFormElement){

    var strCPF = cpf.replace(/\D/g, ''), Soma = 0, Resto, errorCPF;

    if (strCPF == "00000000000" || strCPF == "11111111111" || strCPF == "22222222222" || strCPF == "33333333333" || strCPF == "44444444444" || strCPF == "55555555555" || strCPF == "66666666666" || strCPF == "77777777777" || strCPF == "88888888888" || strCPF == "99999999999"){ 
        errorCPF = 'CPF inválido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        cpfFormElement.setCustomValidity("CPF inválido!");
        return cpfFormElement.reportValidity();
	}

    for (i=1; i<=9; i++){ 
		Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
	}

	Resto = (Soma * 10) % 11;
	 
	if ((Resto == 10) || (Resto == 11)){ 
		Resto = 0;
	}

	if (Resto != parseInt(strCPF.substring(9, 10))){ 
        errorCPF = 'CPF inválido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        cpfFormElement.setCustomValidity("CPF inválido!");
        return cpfFormElement.reportValidity()
	}

	Soma = 0;
	
	for (i = 1; i <= 10; i++){ 
		Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);
	}

	Resto = (Soma * 10) % 11;
	 
	if ((Resto == 10) || (Resto == 11)){  
		Resto = 0;
	}

	if (Resto != parseInt(strCPF.substring(10, 11))){ 
        errorCPF = 'CPF inválido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        cpfFormElement.setCustomValidity("CPF inválido!");
        return cpfFormElement.reportValidity()
	}

	else{
        errorCPF = 'CPF valido!';
        document.getElementById("errorCPF").innerHTML = errorCPF;
        return cpfFormElement.setCustomValidity("")
        
	}
}

const verificaCpf = async () => {

    const formCadastro = document.forms["formCadastro"];
    const cpfFormElement = formCadastro['cpf'];
    const cpf = cpfFormElement.value;
    
    validarCPF(cpf, cpfFormElement);

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