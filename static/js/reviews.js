'use strict';

// create a ajax request for the form input of reviews to flash message "thanks for your review" and then reload
// the section of reviews to be cleared again when it is submitted. 
// submit button does not redirect to new page, it sends success message and reloads section of that page. 
// create event listener for submit button to give success message

let form = document.querySelector('#review-form').addEventListener('submit', (evt) => {
  console.log("IN AJAX");
  evt.preventDefault();
  const reviewText = document.querySelector('#reviews').value
  const recipeId = document.querySelector('#reviews').getAttribute("recipeid")
  console.log(`Review text for ${recipeId}: ${reviewText}`);

  const formInputs = {
    review: document.querySelector('#reviews')
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
