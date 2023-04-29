document.getElementById('idDono').addEventListener('change', function() {
    let selectedOpt = Array.from(this.list.options).find(item => item.value == this.value);
    
    if (typeof selectedOpt == 'undefined') {
        document.getElementById('resultado').innerHTML = '';
    } else {
        document.getElementById('resultado').innerHTML = selectedOpt.textContent;
    }
});