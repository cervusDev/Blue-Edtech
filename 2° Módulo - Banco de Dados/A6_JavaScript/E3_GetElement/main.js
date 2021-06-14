function init() {
    const firstElement = document.getElementById('first-element');
    firstElement.innerText = `Este elemento é a representação de Id "element"`

    const secondElement = document.getElementsByClassName("second-element");
    for (const classe of secondElement) {
        classe.innerText = 'Eu sou um elemento é a representação de class'
    }
}

