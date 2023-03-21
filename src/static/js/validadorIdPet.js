const verificaIdPet = async () => {

    const formAssociar = document.forms["formAssociar"];
    const idPetFormElement = formAssociar['idPet'];
    const idPet = idPetFormElement.value;

    //codigo de comunicação js->flask pra fazer verificação se campo inserido ja tem no sistema

    axios.post('/associar_mais_um_dono_pet_verificando_id', {
            idPet: idPet
        }).then((response) => {
                if (response.data.idPetValido == "true") {
                    console.log(response.data);
         
                    idPetFormElement.setCustomValidity("")
                    document.getElementById("btnCadCadastrar").disabled = false;
    
                } else {
                    idPetFormElement.setCustomValidity("id não castrado!")
                    idPetFormElement.reportValidity()
                    document.getElementById("btnCadCadastrar").disabled = true;
                }
            }, (error) => {
                console.log(error)
            })

}