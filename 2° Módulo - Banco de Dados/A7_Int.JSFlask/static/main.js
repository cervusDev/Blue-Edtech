const cardPokemons = document.querySelectorAll('.card-pokemon')

const pokemonSelecionado = document.querySelector('.pokemon-selecionado')


// Seleção do pokemon 
for (const cardPokemon of cardPokemons) {

    cardPokemon.addEventListener("click", function () {
        const nomePokemon = this.getAttribute('data-nome')

        if (!this.classList.contains("selecionado")) {
            this.classList.add('selecionado')

            pokemonSelecionado.innerHTML = `O último pokemon selecionado foi o <b>${nomePokemon}</b>`
        } else {

            this.classList.remove("selecionado")

            const pokemonSelecionados = document.querySelectorAll(".selecionado")
            //                                não reconhece length
            if (pokemonSelecionados.length >= 1) {
                pokemonSelecionado.innerHTML = `Você desmarcou o pokemon <b>${nomePokemon}</b>. Restantes: <b>${pokemonSelecionados.length}</b>`;
            } else {
                pokemonSelecionado.innerHTML = `selecione um pokemon`
            }

        }
    });

};
