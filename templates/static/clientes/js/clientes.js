function add_carro() {
    var container = document.getElementById("form-carro");

    var html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='Carro' class='form-control' name='carro'></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa'></div> <div class='col-md'><input type='text' placeholder='Ano' class='form-control' name='ano'></div></div>";

    container.innerHTML += html;
}

function exibir_form(tipo){

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')
    console.log(tipo)

    if(tipo == "1"){
        add_cliente.style.display = "block"
        att_cliente.style.display = "none"
        console.log(add_cliente)
        
    } else if(tipo == "2"){
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"
        console.log(att_cliente)
    }
}