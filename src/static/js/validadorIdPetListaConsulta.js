const verificaIdPet = async () => {

    const formConsultaPets = document.forms["formConsultaPets"];
    const idPetFormElement = formConsultaPets['idPet'];
    const idPet = idPetFormElement.value;

    //codigo de comunicação js->flask pra fazer verificação se campo inserido ja tem no sistema

    axios.post('/listar_consulta_pet_verificando_id', {
            idPet: idPet
        }).then((response) => {
                if (response.data.idPetValido == "true") {
                    console.log(response.data);
         
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