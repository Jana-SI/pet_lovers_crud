document.getElementById('cliente').addEventListener('change', function() {
    let selectedOpt = Array.from(this.list.options).find(item => item.value == this.value);
    
    if (typeof selectedOpt == 'undefined') {
        
        document.getElementById('ClienteEsp').innerHTML = '';
        document.getElementById('todosClientes').style.display='inline-block';

    } else {

        var dados = selectedOpt.textContent.split(',');

        dados[1] = dados[1].replace(/(\d{3})(\d{3})(\d{3})(\d{2})/g, "\$1.\$2.\$3\-\$4")

        document.getElementById('todosClientes').style.display='none';
        document.getElementById('ClienteEsp').innerHTML = '<div class="card" id="styleCard"><div class="card-header text-center"><h5 class="card-title">' + dados[0] + '</h5></div><div class="card-body"><p class="card-text">CPF: ' + dados[1] + '</p><p class="card-text">Telefone: ' + dados[2] + '</p><p class="card-text">Quantidade de pets: ' + dados[3] + '</p></div></div>';

    }
});