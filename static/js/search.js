'use strict';

let form = document.querySelector('#search').addEventListener("submit", (evt) => {
  evt.preventDefault();
  let ingredients = document.querySelector('#query').value
  const queryString = new URLSearchParams({ ingredients : ingredients }).toString();
  const url = `/rec-by-ingre?${queryString}`;

  fetch(url)
  .then((response) => response.json())
  .then((recipes) => {
    let searchResults = document.querySelector("#search-results")
    
    // remove all divs with id search-results
    while (searchResults.firstChild) {
      searchResults.firstChild.remove();
    }
    
    for (const recipe of recipes) {
        searchResults.insertAdjacentHTML(
          "beforeend",
          `<div class="col-12 col-lg-4">
          <div class="card h-80 text-center box-shadow mb-3 mx-auto my-5" style="width: 25rem;">
            <img src="${recipe.image_url}" class="card-img-top">
            <div class="card-body">
              <a class="card-title"  style="text-decoration: none;" href="/recipe/${recipe.id}">${recipe.title}</a>
              <hr>
              <button class="btn btn-outline-danger my-2 my-sm-0" id="fav-btn" type="button" data-recipe-id="${recipe.id}">Favorite</button>
            </div>
          </div>
        </div>`
          )
      }
  });
});