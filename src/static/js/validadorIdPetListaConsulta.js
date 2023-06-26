const verificaIdPet = async () => {

    const formConsultaPets = document.forms["formConsultaPets"];
    const idPetFormElement = formConsultaPets['idPet'];
    const idPet = idPetFormElement.value;

    if (!idPet) {
        errorIdPet = 'Campo ID PET está vazio!!';
        document.getElementById("errorIdPet").innerHTML = errorIdPet;
        document.getElementById("btnPesquisar").disabled = true;
        document.getElementById("errorIdPet").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px; margin-bottom: 16px;';
        idPetFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
    }

    else {

        axios.post('/listar_consulta_pet_verificando_id', {
            idPet: idPet
        }).then((response) => {
            if (response.data.idPetValido == "true") {

                errorIdPet = '';
                document.getElementById("errorIdPet").innerHTML = errorIdPet;
                document.getElementById("errorIdPet").style.cssText = '';
                idPetFormElement.style.cssText = '';
                document.getElementById("btnPesquisar").disabled = false;

            } else {
                errorIdPet = 'ID PET não castrado!';
                document.getElementById("errorIdPet").innerHTML = errorIdPet;
                document.getElementById("errorIdPet").style.cssText = 'color: red; border: 2px solid red; text-align: center; background: #fee; border-radius: 10px; padding: 10px; margin-bottom: 16px;';
                document.getElementById("btnPesquisar").disabled = true;
                idPetFormElement.style.cssText = 'color: red; border: 2px solid red; background: #fee;';
            }
        }, (error) => {
            console.log(error)
        })
    }

}