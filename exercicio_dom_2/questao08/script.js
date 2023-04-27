const getElements = () => {
    const select = document.getElementById('selectOption')
    const display =  document.getElementById('display')
    const input = document.getElementById('texto')
    const button = document.getElementById('inserir')

    return { button, select, display, input }
}



const opcaoRepetida = (content) => {
    const arrayOption = Array.from(document.getElementsByTagName("option"))

    return arrayOption.some(option => option.value === content)
}

const temCincoOpcoes = () => {
    const arrayOption = Array.from(document.getElementsByTagName("option"))
    return arrayOption.length === 5
}

function inserirOpcoes({ select, display, input }) {
    const content = input.value
    const option = document.createElement('option')
    display.innerHTML = ''
    
    if(opcaoRepetida(content)) {
        display.innerHTML = 'Opção já inserida'
    } else if (temCincoOpcoes()) {
        display.innerHTML = 'Limite de 5 opções atingidas'
    } else if (content.length == 0){
        display.innerHTML = 'Digite algum texto'
    } else {
        option.value = content
        option.innerText = content
        select.appendChild(option)
    }
    input.value = ''
}

const { select, display, input, button } = getElements()

input.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') { 
      event.preventDefault(); 
      button.click();
    }
  });


button.addEventListener('click', () => inserirOpcoes({select, display, input}))


