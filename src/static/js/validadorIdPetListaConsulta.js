const verificaIdPet = async () => {

    const formConsultaPets = document.forms["formConsultaPets"];
    const idPetFormElement = formConsultaPets['idPet'];
    const idPet = idPetFormElement.value;

    if (!idPet) {
        idPetFormElement.setCustomValidity("Campo id pet está vazio!")
        idPetFormElement.reportValidity()
    }

    else {

        axios.post('/listar_consulta_pet_verificando_id', {
            idPet: idPet
        }).then((response) => {
            if (response.data.idPetValido == "true") {

                idPetFormElement.setCustomValidity("")
                document.getElementById("btnPesquisar").disabled = false;

            } else {
                idPetFormElement.setCustomValidity("id não castrado!")
                idPetFormElement.reportValidity()
                document.getElementById("btnPesquisar").disabled = true;
            }
        }, (error) => {
            console.log(error)
        })
    }

}