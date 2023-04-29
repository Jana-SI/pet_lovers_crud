const verificaIdDono = async () => {

    const formAgendar = document.forms["formAgendar"];
    const idDonoFormElement = formAgendar['idDono'];
    const idDono = idDonoFormElement.value;

    //codigo de comunicação js->flask pra fazer verificação se campo inserido ja tem no sistema

    axios.post('/agendar_consulta_verificando_id', {
            idDono: idDono
        }).then((response) => {
                if (response.data.idDonoValido == "true") {
                    console.log(response.data);
         
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