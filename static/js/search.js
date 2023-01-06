'use strict';

let form = document.querySelector('#search').addEventListener('submit', (evt) => {
  evt.preventDefault();
  let ingredients = document.querySelector('#query').value
  const queryString = new URLSearchParams({ ingredients : ingredients }).toString();
  const url = `/rec-by-ingre?${queryString}`;

  fetch(url)
  .then((response) => response.json())
  .then((recipes) => {
    let searchResults = document.querySelector("#search-results")
    
    while (searchResults.hasChildNodes()) {
      searchResults.removeChild(searchResults.firstElementChild);
    }
    
    for (const recipe of recipes) {
      searchResults.insertAdjacentHTML(
        "beforeend",
        `<li><a href="/recipe-api/${recipe.id}">${recipe.name}</a> ---
        <button id="fav-btn" data-recipe-id="${recipe.id}">Favorite</button></li>`
        )
      }
  });
});
// to use for extracting data
// `<li><a href="/recipe/${recipe.id}" data=${recipe} >${recipe.name}</a>