document.getElementById('idPet').addEventListener('change', function() {
    let selectedOpt = Array.from(this.list.options).find(item => item.value == this.value);
    
    if (typeof selectedOpt == 'undefined') {
        document.getElementById('resultadoPet').innerHTML = '';
    } else {
        document.getElementById('resultadoPet').innerHTML = selectedOpt.textContent;
    }
});


document.getElementById('donosPet').addEventListener('change', function() {
    let selectedOpt = Array.from(this.list.options).find(item => item.value == this.value);
    
    if (typeof selectedOpt == 'undefined') {
        document.getElementById('resultadoDono').innerHTML = '';
    } else {
        document.getElementById('resultadoDono').innerHTML = selectedOpt.textContent;
    }
});