'use strict';

let form = document.querySelector('#review-form').addEventListener('submit', (evt) => {
  evt.preventDefault();
  const reviewText = document.querySelector('#reviews').value
  const recipeId = document.querySelector('#reviews').getAttribute("recipeid")

  const formInputs = {
    review: reviewText
  };
  
  fetch(`/review/${recipeId}`, {
    method: 'POST',
    body: JSON.stringify(formInputs),
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => response.json())
    .then((responseJson) => {
      let lbl = document.querySelector("#my-label")
      lbl.innerHTML = responseJson.status;
    });
});
