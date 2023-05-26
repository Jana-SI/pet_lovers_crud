const verificaIdPet = async () => {

    const formListaPets = document.forms["formListaPets"];
    const idPetFormElement = formListaPets['idPet'];
    const idPet = idPetFormElement.value;

    if (!idPet) {
        idPetFormElement.setCustomValidity("Campo id pet está vazio!")
        idPetFormElement.reportValidity()
    }

    else {

        axios.post('/listar_pet_verificando_id', {
            idPet: idPet
        }).then((response) => {
            if (response.data.idPetValido == "true") {

                idPetFormElement.setCustomValidity("")

            } else {
                idPetFormElement.setCustomValidity("id não castrado!")
                idPetFormElement.reportValidity()
            }
        }, (error) => {
            console.log(error)
        })
    }

}