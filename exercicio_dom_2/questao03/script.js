

document.getElementById('showImage').addEventListener('click', () => {
    showImage()
})

const showImage = () => {
    const url = document.getElementById('url').value
    const result = document.getElementById('result')
    const newImage = document.createElement('img')
    newImage.src = url
    newImage.style.width = '200px'
    newImage.style.height = '200px'

    result.appendChild(newImage)

} 