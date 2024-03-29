function calcularIdade(nascimento) {
    const dataAtual = new Date();
    const anoAtual = dataAtual.getFullYear();
    const mesAtual = dataAtual.getMonth() + 1;
    const diaAtual = dataAtual.getDate();

    const [anoNascimento, mesNascimento, diaNascimento] = nascimento.split('-').map(Number);

    let idade = anoAtual - anoNascimento;

    if (mesAtual < mesNascimento || (mesAtual === mesNascimento && diaAtual < diaNascimento)) {
        idade--; // Ajuste na idade se ainda não completou o ano atual
    }

    return idade;
}

const verificarData = async () => {

    const nascimento = document.getElementById('nascimento').value;
    const formCadastro = document.forms["formAtualiza"];
    const nascFormElement = formCadastro['nascimento'];
    var errorData;

    if (!nascimento) {
        errorData = "campo Data está vazio !!";
        document.getElementById("errorData").innerHTML = errorData;
        document.getElementById("errorData").style.cssText = 'display: block;color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
        nascFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
        document.getElementById("btnCadCadastrar").disabled = true;
    }

    else {

        let idade = calcularIdade(nascimento);

        if (idade < 0) {
            errorData = "Data de nascimento inválida, idade negativa!";
            document.getElementById("errorData").innerHTML = errorData;
            document.getElementById("errorData").style.cssText = 'display: block;color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
            nascFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
            document.getElementById("btnCadCadastrar").disabled = true;
        }

        else if (idade > 100) {
            errorData = "Data de nascimento inválida, idade passou dos 100 anos!";
            document.getElementById("errorData").innerHTML = errorData;
            document.getElementById("errorData").style.cssText = 'display: block;color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
            nascFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
            document.getElementById("btnCadCadastrar").disabled = true;
        }

        else if (idade == '') {
            errorData = '';
            document.getElementById("errorData").innerHTML = errorData;
            document.getElementById("errorData").style.cssText = '';
            nascFormElement.style.cssText = ''
            document.getElementById("btnCadCadastrar").disabled = true;
        }

        else {
            errorData = idade + ' anos';
            document.getElementById("errorData").innerHTML = errorData;
            document.getElementById("errorData").style.cssText = 'display: block;';
            nascFormElement.style.cssText = '';
            document.getElementById("btnCadCadastrar").disabled = true;
        }
    }
}