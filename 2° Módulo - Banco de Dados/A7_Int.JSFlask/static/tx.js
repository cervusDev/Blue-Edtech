const cardPokemons = document.querySelectorAll('.lista-pokemons')

const pokemonSelecionado = document.querySelector('.pokemon-selecionado')

// click 
for (const cardPokemon of cardPokemons) {

    cardPokemon.addEventListener('click', function (event) {
        const nomePokemon = document.querySelector('.card-pokemon')
        nomePokemon.getAttribute('[data-nome]')

        if (!nomePokemon.classList.contains()) {

            nomePokemon.classList.add('selecionado')

            pokemonSelecionado.innerHTML = `O último pokemon selecionado foi o <b>${pokemon.nome}</b>`
        } else {

            nomePokemon.classList.remove('slecionado')

            const pokemonSelecionados = document.querySelectorAll('.selecionado')

            if (pokemonSelecionado.lenght >= 1) {
                pokemonSelecionado.innerHTML = `Você desmarcou o pokemon <b>${nomePokemon}</b>. Restantes: <b>${pokemonSelecionados.lenght}</b>`;
            } else {
                pokemonSelecionado.innerHTML = `selecione um pokemon`
            }

        }
    })


}
