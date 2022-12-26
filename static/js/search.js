'use strict';

let form = document.querySelector('#search').addEventListener('submit', (evt) => {
    evt.preventDefault();
    let ingredients = document.querySelector('#query').value
    const queryString = new URLSearchParams({ ingredients : ingredients }).toString();
    const url = `/rec-by-ingre?${queryString}`;

    fetch(url)
    .then((response) => response.text())
    .then((status) => {
      let results = document.querySelector("#search-results")
    results.innerHTML = status
    });
  });