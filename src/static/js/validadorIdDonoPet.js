const verificaIdDono = async () => {

    const formAgendar = document.forms["formAgendar"];
    const idDonoFormElement = formAgendar['idDono'];
    const idDono = idDonoFormElement.value;

    if (!idDono) {
        errorIdDono = 'Campo ID Dono está vazio!!';
        document.getElementById("errorIdDono").innerHTML = errorIdDono;
        document.getElementById("btnAgendar").disabled = true;
        document.getElementById("errorIdDono").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
        idDonoFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
        document.getElementById("resultado").style.cssText = 'display: none;';
    }

    else {

        axios.post('/agendar_consulta_verificando_id', {
            idDono: idDono
        }).then((response) => {
            if (response.data.idDonoValido == "true") {

                errorIdDono = '';
                document.getElementById("errorIdDono").innerHTML = errorIdDono;
                document.getElementById("errorIdDono").style.cssText = '';
                document.getElementById("resultado").style.cssText = 'display: block;';
                idDonoFormElement.style.cssText = '';
                document.getElementById("btnAgendar").disabled = false;

            } else {
                document.getElementById("btnAgendar").disabled = true;
                errorIdDono = 'ID PET não castrado!';
                document.getElementById("errorIdDono").innerHTML = errorIdDono;
                document.getElementById("btnAgendar").disabled = true;
                document.getElementById("errorIdDono").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
                idDonoFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
                document.getElementById("resultado").style.cssText = 'display: none;';
            }
        }, (error) => {
            console.log(error)
        })
    }

}