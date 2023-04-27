

document.getElementById('verify').addEventListener('click', () => {
    isCheckboxChecked()
})


const isCheckboxChecked = () => {
    const checkboxs = document.getElementsByName('checkbox1')
    for (let i = 0; i < checkboxs.length; i++) {
        if(checkboxs[i].checked) {
            console.log("Um checkbox foi marcado")
            return
        }
    }
    console.log("Nenhum checkbox foi marcado")
    return    
}