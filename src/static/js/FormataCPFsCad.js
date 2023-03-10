const donos= document.querySelector("#listaDonos")

const options = [...donos.options]

options.forEach((option) => {
    cpf = option.value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/g, "\$1.\$2.\$3\-\$4")
    option.value = cpf
})