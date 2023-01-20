'use strict';

// create click event target
document.addEventListener('click', (evt) => {
  const favBtn = evt.target.closest('#fav-btn');

  // on CLICK target, make request to db 
  if (favBtn) {
    if (favBtn.innerHTML == "Unfavorite") {
      // if it's already favorited, remove it from user's favorite
      const url = `/unfavorite/${favBtn.dataset.recipeId}`;
      fetch(url)
      .then((response) => response.json())
      .then((resp) => {
        if (resp.status == "Success") {
          console.log(`${resp.status} - ${resp.msg}`);
          favBtn.innerHTML = "Favorite";
        } else {
          console.log(`${resp.status} - ${resp.msg}`);
        }
      });
    } else {
      // if not favorited, add to user's favorite
      const url = `/favorites/${favBtn.dataset.recipeId}`;
      fetch(url)
      .then((response) => response.json())
      .then((resp) => {
        if (resp.status == "Success") {
          console.log(`${resp.status} - ${resp.msg}`);
          favBtn.innerHTML = "Unfavorite";
        } else {
          console.log(`${resp.status} - ${resp.msg}`);
        }
      });
    }
  }
});
  