/*Altere o código anterior validando se o campo foi preenchido. Para isso, verifique se o conteúdo passado é uma string vazia e exiba uma mensagem de erro nesse caso. Você pode exibir um alert do JS ou mesmo escrever na div algo com a fonte “vermelha”.*/

document.addEventListener('DOMContentLoaded', function () {
        var botaoExibir = document.getElementById('botaoExibir');
        botaoExibir.addEventListener('click', exibirConteudo);
    });

function exibirConteudo() {
    const caixaDeTexto = document.getElementById('caixaDeTexto');
    const conteudo = caixaDeTexto.value
    const display = document.getElementById('conteudo') 
    const selectOption = document.getElementById("selectOption").value

    display.innerHTML =   formatContent(conteudo, selectOption)
}


function formatContent(string, option) {
    switch (option) {
        case 'maiuscula':        
            return string.toUpperCase()
        case 'minuscula':        
            return string.toLowerCase()
    }
}

//innerHTML modifica ou retorna todo o conteúdo da tag que está sendo trabalhada