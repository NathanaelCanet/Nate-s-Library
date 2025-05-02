document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('input[name="query"]');
    const searchType = document.querySelector('select[name="type"]');
    const suggestionsBox = document.getElementById('suggestions');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value;
        const type = searchType.value;

        if (query.length > 1) {
            fetch(`/autocomplete?type=${type}&query=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsBox.innerHTML = '';
                    data.forEach(item => {
                        const suggestion = document.createElement('div');
                        suggestion.textContent = item;
                        suggestion.addEventListener('click', function () {
                            searchInput.value = item;
                            suggestionsBox.innerHTML = '';
                        });
                        suggestionsBox.appendChild(suggestion);
                    });
                });
        } else {
            suggestionsBox.innerHTML = '';
        }
    });
});