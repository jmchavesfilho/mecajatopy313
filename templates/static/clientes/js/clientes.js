function add_carro() {
    var container = document.getElementById("form-carro");

    var html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='Carro' class='form-control' name='carro'></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa'></div> <div class='col-md'><input type='text' placeholder='Ano' class='form-control' name='ano'></div></div>";

    container.innerHTML += html;
}

function exibir_form(tipo) {

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')
    console.log(tipo)

    if (tipo == "1") {
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
        console.log(add_cliente)

    } else if (tipo == "2") {
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"
        console.log(att_cliente)
    }
}
function dados_cliente() {
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {   // troquei cliente por clientes
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function (result) {
        return result.json()
    }).then(function (data) {

        console.log(data)
    })
}

//video parado no minuto 40:40 24/10/2024