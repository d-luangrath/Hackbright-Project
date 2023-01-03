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
        console.log(recipe.name, recipe.id)
        searchResults.insertAdjacentHTML("beforeend", `<li><a href="/recipe-api/${recipe.id}">${recipe.name}</li>`)
      }
    });
  });