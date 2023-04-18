function fijarSearch() {
    const inputBusqueda = document.getElementById("busqueda");
    
    inputBusqueda.style.transition= "1s";
    inputBusqueda.style.opacity = "100%";
    inputBusqueda.style.width = "200px";
    inputBusqueda.style.height = "40px"
    inputBusqueda.style.borderRadius = "20px 0 0 20px"
    inputBusqueda.style.textAlign = "center";
    inputBusqueda.style.fontSize = "15px";
    inputBusqueda.style.fontFamily = "'Times New Roman', Times, serif";
    inputBusqueda.style.boxShadow = "2px 2px 4px rgba(0, 0, 0, 0.3)";
    inputBusqueda.style.border = "none";
    inputBusqueda.style.outline = "none";
    inputBusqueda.focus();

    const botonBusqueda = document.getElementById("btn-enviar");
    botonBusqueda.style.transition= "1s";
    botonBusqueda.style.opacity = "100%";
    botonBusqueda.style.width = "60px";
    botonBusqueda.style.height = "40px"
    botonBusqueda.style.borderRadius = "0 20px 20px 0"
    botonBusqueda.style.textAlign = "center";
    botonBusqueda.style.fontSize = "15px";
    botonBusqueda.style.fontFamily = "'Times New Roman', Times, serif";
    botonBusqueda.style.boxShadow = "2px 2px 4px rgba(0, 0, 0, 0.3)";
    botonBusqueda.style.border = "none";
}

function ocultarSearch() {
    const inputBusqueda = document.getElementById("busqueda");
    
    inputBusqueda.style.transition = "1s";
    inputBusqueda.style.opacity = "0%";
    inputBusqueda.style.width = "0";

    const botonBusqueda = document.getElementById("btn-enviar");
    botonBusqueda.style.transition = "1s";
    botonBusqueda.style.opacity = "0%";
    botonBusqueda.style.width = "0";
  }