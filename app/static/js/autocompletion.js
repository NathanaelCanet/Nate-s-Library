
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const searchType = document.getElementById('search-type');
    const suggestionsBox = document.getElementById('suggestions');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value;
        const type = searchType.value;

        if (query.length > 1) { // Ne commence la recherche qu'après 2 caractères
            fetch(`/autocomplete?type=${type}&query=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsBox.innerHTML = ''; // Vide les suggestions précédentes
                    data.forEach(item => {
                        const suggestion = document.createElement('div');
                        suggestion.textContent = item;
                        suggestion.addEventListener('click', function () {
                            searchInput.value = item; // Remplit le champ avec la suggestion
                            suggestionsBox.innerHTML = ''; // Cache les suggestions
                        });
                        suggestionsBox.appendChild(suggestion);
                    });
                });
        } else {
            suggestionsBox.innerHTML = ''; // Cache les suggestions si la saisie est trop courte
        }
    });

    // Cache les suggestions si l'utilisateur clique en dehors
    document.addEventListener('click', function (e) {
        if (!suggestionsBox.contains(e.target) && e.target !== searchInput) {
            suggestionsBox.innerHTML = '';
        }
    });
});
