const verificaIdPet = async () => {

    const formAssociar = document.forms["formAssociar"];
    const idPetFormElement = formAssociar['idPet'];
    const idPet = idPetFormElement.value;

    if (!idPet) {
        errorIdPet = 'Campo ID PET está vazio!!';
        document.getElementById("errorIdPet").innerHTML = errorIdPet;
        document.getElementById("btnCadCadastrar").disabled = true;
        document.getElementById("errorIdPet").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
        idPetFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
        document.getElementById("resultadoPet").style.cssText = 'display: none;';
    }

    else {

        axios.post('/associar_mais_um_dono_pet_verificando_id', {
            idPet: idPet
        }).then((response) => {
            if (response.data.idPetValido == "true") {
                errorIdPet = '';
                document.getElementById("errorIdPet").innerHTML = errorIdPet;
                document.getElementById("errorIdPet").style.cssText = '';
                document.getElementById("resultadoPet").style.cssText = 'display: block;';
                idPetFormElement.style.cssText = '';
                document.getElementById("btnCadCadastrar").disabled = false;

            } else {
                document.getElementById("btnCadCadastrar").disabled = true;
                errorIdPet = 'ID PET não castrado!';
                document.getElementById("errorIdPet").innerHTML = errorIdPet;
                document.getElementById("btnCadCadastrar").disabled = true;
                document.getElementById("errorIdPet").style.cssText = 'color: red; border: 2px solid red; background: #fee; border-radius: 10px; padding: 10px;';
                idPetFormElement.style.cssText = 'color: red; border: 2px solid red;background: #fee;'
                document.getElementById("resultadoPet").style.cssText = 'display: none;';
            }
        }, (error) => {
            console.log(error)
        })
    }

}