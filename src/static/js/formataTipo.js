function tipoFormatado(tipo) {
    if (tipo.toLowerCase() === "exotico") {
      return "exótico";
    }
    if (tipo.toLowerCase() === "nao-declarado") {
      return "não declarado";
    }
    return tipo;
  }
  
  const tipoElements = document.querySelectorAll('.tipo');
  
  for (let i = 0; i < tipoElements.length; i++) {
    const tipo = tipoElements[i].innerText;
    tipoElements[i].textContent = tipoFormatado(tipo);
  }
  