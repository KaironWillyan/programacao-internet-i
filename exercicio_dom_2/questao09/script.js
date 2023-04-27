const getElements = () => {
    const select = document.getElementById('selectOption')
    const display =  document.getElementById('display')
    const input = document.getElementById('texto')
    const buttonInserir = document.getElementById('inserir')
    const buttonRemover = document.getElementById('remover')

    return { buttonInserir, buttonRemover, select, display, input }
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

function removerOpcoes ( { select } ) {
    const selectedOptions = select.selectedOptions
    const allOptions = select.options

    const selectedOptionsArray = Array.from(selectedOptions)
    const allOptionsArray = Array.from(allOptions)
    
    allOptionsArray.forEach((option, index) => {
        if(selectedOptionsArray.includes(option)){
            select.removeChild(allOptions[index])
        }
    });
} 

const { select, display, input, buttonInserir, buttonRemover } = getElements()

input.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') { 
      event.preventDefault(); 
      buttonInserir.click();
    }
  });

buttonInserir.addEventListener('click', () => inserirOpcoes({select, display, input}))

buttonRemover.addEventListener('click', () => removerOpcoes({ select }))


