const verificaIdDono = async () => {

    const formAgendar = document.forms["formAgendar"];
    const idDonoFormElement = formAgendar['idDono'];
    const idDono = idDonoFormElement.value;

    if(!idDono){
        idDonoFormElement.setCustomValidity("Campo id dono está vazio!")
        idDonoFormElement.reportValidity()
    }

    else{

        axios.post('/agendar_consulta_verificando_id', {
            idDono: idDono
        }).then((response) => {
            if (response.data.idDonoValido == "true") {

                idDonoFormElement.setCustomValidity("")
                document.getElementById("btnAgendar").disabled = false;

            } else {
                idDonoFormElement.setCustomValidity("id não castrado!")
                idDonoFormElement.reportValidity()
                document.getElementById("btnAgendar").disabled = true;
            }
        }, (error) => {
            console.log(error)
        })
    }

}