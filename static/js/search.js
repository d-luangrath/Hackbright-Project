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
    

// create click event target
document.addEventListener('click', function(evt) {
  const favBtn = evt.target.closest('#fav-btn');
  
  // on CLICK target, make request to db 
  if (favBtn) {
    const url = `/favorite/${favBtn.dataset.recipeId}`;

    fetch(url)
    .then((response) => response.json())
    .then((resp) => {
      if (resp.status == "Success") {
        console.log(`${resp.status} - ${resp.msg}`);
        favBtn.innerHTML = "Favorited";
        favBtn.disabled = true;
      } else {
        console.log(`${resp.status} - ${resp.msg}`);
        favBtn.innerHTML = "It looks like it was already favorited earlier...";
        favBtn.disabled = true;
      }
    });
  }
});
