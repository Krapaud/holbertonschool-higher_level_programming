#!/usr/bin/node
// Script to fetch and list all Star Wars movie titles
async function displayTitle () {
  const element = document.getElementById('list_movies');
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const data = await response.json();

  for (const movie of data.results) {
    const newItem = document.createElement('li');
    newItem.textContent = movie.title;
    element.appendChild(newItem);
  }
}
displayTitle();
