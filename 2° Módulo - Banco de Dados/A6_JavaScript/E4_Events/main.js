const botao = document.querySelector('.wrapper-button #botao')

function clicar() {
    alert("Você clicou no botão")
};

botao.addEventListener("click", clicar);
botao.innerHTML = 'clique aqui'