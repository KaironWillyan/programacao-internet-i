const getElements = () => {
    const select = document.getElementById('selectOption')
    const display =  document.getElementById('display')
    const input = document.getElementById('texto')
    const button = document.getElementById('inserir')

    return { button, select, display, input }
}

function inserirOpcoes({ select, display, input }) {
    console.log('sada')
    const content = input.value
    const option = document.createElement('option')
    display.innerHTML = ''
    
    if(content.length) {
        option.value = content
        option.innerText = content
        
        select.appendChild(option)
    } else {
        display.innerHTML = 'Digite algum texto'
    }
    input.value = ''
}

const { select, display, input, button } = getElements()
button.addEventListener('click', () => inserirOpcoes({select, display, input}))


