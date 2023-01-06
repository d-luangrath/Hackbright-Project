'use strict';

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
  
