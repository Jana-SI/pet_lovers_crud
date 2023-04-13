const verificaIdPet = async () => {

    const formListaPets = document.forms["formListaPets"];
    const idPetFormElement = formListaPets['idPet'];
    const idPet = idPetFormElement.value;

    //codigo de comunicação js->flask pra fazer verificação se campo inserido ja tem no sistema

    axios.post('/listar_pet_verificando_id', {
            idPet: idPet
        }).then((response) => {
                if (response.data.idPetValido == "true") {
                    console.log(response.data);
         
                    idPetFormElement.setCustomValidity("")
    
                } else {
                    idPetFormElement.setCustomValidity("id não castrado!")
                    idPetFormElement.reportValidity()
                }
            }, (error) => {
                console.log(error)
            })

}