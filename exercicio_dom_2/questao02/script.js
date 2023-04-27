/*Crie uma página com 2 campos e um botão. Crie também um script que realize alguma
operação matemática entre os dois campos. Além disso, aceite apenas números fazendo
a validação com a função isNaN().*/

const buttonCalculate = document.getElementById('calculate')

buttonCalculate.addEventListener('click', () => calculator())


function calculator() {
    console.log('aaaaaaa')
    const valor1 = Number(document.getElementById('number1').value)
    const valor2 = Number(document.getElementById('number2').value)
    const display = document.getElementById('display')
    const operation = document.getElementById('selectOption').value
    let result

    console.log(valor1, valor2, operation)

    if(isNumber(valor1, valor2)) {
        result = 'Insira apenas números'
    } else {
        result = String(calculate(operation, valor1, valor2)) 
    }
    display.innerHTML = result
}

const isNumber = (valor1, valor2) => isNaN(valor1) || isNaN(valor2)

function calculate(operation, valor1, valor2) {
    switch (operation) {
        case '+':
            return valor1 + valor2
        case '-':
            return valor1 - valor2
        case '*':
            return valor1 * valor2
        case '/':
            return valor1 / valor2
    }
}