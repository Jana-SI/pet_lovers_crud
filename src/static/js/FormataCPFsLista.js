const clientes= document.querySelector("#listaCliente")

const options = [...clientes.options]

options.forEach((option) => {
    var cpf = option.value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/g, "\$1.\$2.\$3\-\$4")
    option.value = cpf
})

const cpfs = document.querySelectorAll('.formatarCPF');

cpfs.forEach(element => {

  element.textContent = element.innerText.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/g, "\$1.\$2.\$3\-\$4");
  
});