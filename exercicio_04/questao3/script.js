var botao = document.getElementById("botao");
var botaoLimpar = document.getElementById("limpar");
var paragrafo = document.getElementById("paragrafo");


// adicione um evento de clique ao botão
botao.addEventListener("click", function() {
    // altere o texto do parágrafo
    paragrafo.textContent = "O texto deste parágrafo foi alterado!";
});


botaoLimpar.addEventListener("click", function() {
    paragrafo.textContent = "";

})



